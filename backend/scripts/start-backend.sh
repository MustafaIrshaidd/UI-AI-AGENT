#!/bin/bash

echo "🚀 Starting UI AI Agent Backend..."

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this script from the backend directory."
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

# Start PostgreSQL and pgAdmin if not already running
echo "📦 Checking Docker containers..."
if ! cd .. && docker compose ps | grep -q "ui_ai_agent_postgres.*Up"; then
    echo "🐘 Starting PostgreSQL and pgAdmin..."
    cd .. && docker compose up -d postgres pgadmin
    
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
    
    cd backend
else
    echo "✅ PostgreSQL and pgAdmin are already running"
    cd backend
fi

# We're already in the backend directory

# Install dependencies if needed
echo "📦 Checking Python dependencies..."
if [ ! -d ".venv" ]; then
    echo "🔧 Installing dependencies..."
    poetry install
fi

# Set environment variables
export DATABASE_URL="postgresql://postgres:postgres@localhost:5434/ui_ai_agent"
export FRONT_END_URL="http://localhost:3000"
export ENVIRONMENT="development"

echo "🌐 Starting FastAPI server with GraphQL..."
echo "📊 GraphQL Playground: http://localhost:8000/graphql"
echo "📈 pgAdmin Dashboard: http://localhost:5050 (admin@admin.com / admin)"
echo "🔗 API Documentation: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the server
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload 