#!/bin/bash

echo "🚀 Starting UI AI Agent Backend..."

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ Error: docker-compose.yml not found. Please run this script from the project root directory."
    exit 1
fi

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

# Ensure required ports are free before starting
if command -v lsof >/dev/null 2>&1; then
    echo "🧹 Ensuring port 8000 is free..."
    PIDS=$(lsof -ti tcp:8000)
    if [ -n "$PIDS" ]; then
        echo "⚠️  Port 8000 is in use by PID(s): $PIDS — attempting to free..."
        kill $PIDS 2>/dev/null || true
        sleep 1
        PIDS=$(lsof -ti tcp:8000)
        if [ -n "$PIDS" ]; then
            echo "⚠️  Force killing PID(s) on port 8000: $PIDS"
            kill -9 $PIDS 2>/dev/null || true
        fi
    fi
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
cd backend
poetry install

# Set environment variables
export DATABASE_URL="postgresql://postgres:X3xEqWvKukwKNlWs@localhost:5434/ui_ai_agent"
export FRONTEND_URL="http://localhost:3000"
export ENVIRONMENT="development"
export DEBUG="true"

echo ""
echo "🔥 Starting FastAPI server with GraphQL..."
echo "📊 GraphQL Playground: http://localhost:8000/graphql"
echo "🔗 API Documentation: http://localhost:8000/docs"
echo "🗄️ pgAdmin: http://localhost:5050"
echo ""
echo "Press Ctrl+C to stop the backend server"
echo ""

# Start the server
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload 