#!/bin/bash

echo "🚀 Starting UI AI Agent with GraphQL and PostgreSQL..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Start PostgreSQL and pgAdmin with Docker Compose
echo "📦 Starting PostgreSQL and pgAdmin..."
docker-compose up -d

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."
sleep 10

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
sleep 3

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