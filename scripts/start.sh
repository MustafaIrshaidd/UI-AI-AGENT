#!/bin/bash

# Cleanup function to stop all services
cleanup() {
    echo ""
    echo "🛑 Shutting down services..."
    
    # Kill backend process
    if [ ! -z "$BACKEND_PID" ]; then
        echo "🔄 Stopping FastAPI backend..."
        kill $BACKEND_PID 2>/dev/null
    fi
    
    # Kill frontend process
    if [ ! -z "$FRONTEND_PID" ]; then
        echo "🔄 Stopping Next.js frontend..."
        kill $FRONTEND_PID 2>/dev/null
    fi
    
    # Stop Docker containers
    echo "🔄 Stopping Docker containers..."
    docker compose down
    
    echo "✅ All services stopped!"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

echo "🚀 Starting UI AI Agent with GraphQL and PostgreSQL..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    echo "💡 On macOS, you can start Docker Desktop from Applications or run:"
    echo "   open -a Docker"
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker compose &> /dev/null; then
    echo "❌ Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

# Stop any existing containers to ensure clean start
echo "🧹 Stopping any existing containers..."
docker compose down > /dev/null 2>&1

# Start PostgreSQL and pgAdmin with Docker Compose
echo "📦 Starting PostgreSQL and pgAdmin..."
docker compose up -d postgres pgadmin

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."
max_attempts=30
attempt=0

while [ $attempt -lt $max_attempts ]; do
    if docker compose exec -T postgres pg_isready -U postgres > /dev/null 2>&1; then
        echo "✅ PostgreSQL is ready!"
        break
    fi
    
    attempt=$((attempt + 1))
    echo "⏳ Waiting for PostgreSQL... (attempt $attempt/$max_attempts)"
    sleep 2
done

if [ $attempt -eq $max_attempts ]; then
    echo "❌ PostgreSQL failed to start within expected time."
    echo "💡 Check Docker logs: docker compose logs postgres"
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
cd backend
poetry install

# Set environment variables
export DATABASE_URL="postgresql://postgres:postgres@localhost:5434/ui_ai_agent"
export FRONTEND_URL="http://localhost:3000"
export ENVIRONMENT="development"
export DEBUG="true"

# Start FastAPI server in background
echo "🔥 Starting FastAPI server with GraphQL..."
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!

# Wait a moment for backend to start
echo "⏳ Waiting for backend to start..."
sleep 5

# Check if backend is running
if ! curl -s http://localhost:8000/health > /dev/null; then
    echo "❌ Backend failed to start. Check logs above."
    exit 1
fi

echo "✅ Backend is running!"

# Go back to project root and start frontend
cd ..
echo "🎨 Starting Next.js frontend..."
cd frontend

# Install frontend dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
fi

# Start Next.js frontend
echo "🚀 Starting Next.js development server..."
npm run dev &
FRONTEND_PID=$!

# Wait a moment for frontend to start
sleep 3

# Check if frontend is running
if ! curl -s http://localhost:3000 > /dev/null; then
    echo "⚠️  Frontend may still be starting up..."
else
    echo "✅ Frontend is running!"
fi

echo ""
echo "🎉 UI AI Agent is starting up!"
echo ""
echo "📊 Services:"
echo "   🌐 Frontend: http://localhost:3000"
echo "   🔥 Backend: http://localhost:8000"
echo "   📊 Dashboard: http://localhost:8000/dashboard"
echo "   🔍 GraphQL: http://localhost:8000/graphql"
echo "   📚 API Docs: http://localhost:8000/docs"
echo "   🗄️ pgAdmin: http://localhost:5050"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Wait for user to stop
wait 