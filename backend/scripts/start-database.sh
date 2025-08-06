#!/bin/bash

echo "🐘 Starting Database Services..."

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
cd .. && docker compose down > /dev/null 2>&1

# Start PostgreSQL and pgAdmin
echo "📦 Starting PostgreSQL and pgAdmin..."
cd .. && docker compose up -d postgres pgadmin && cd backend

# Wait for PostgreSQL to be ready
echo "⏳ Waiting for PostgreSQL to be ready..."
max_attempts=30
attempt=0

while [ $attempt -lt $max_attempts ]; do
    if cd .. && docker compose exec -T postgres pg_isready -U postgres > /dev/null 2>&1; then
        echo "✅ PostgreSQL is ready!"
        cd backend
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

# Check if services are running
if cd .. && docker compose ps | grep -q "ui_ai_agent_postgres.*Up"; then
    cd backend
    echo "✅ PostgreSQL is running on localhost:5434"
    echo "✅ pgAdmin is running on http://localhost:5050"
    echo ""
    echo "📊 Database Access:"
    echo "   Host: localhost"
    echo "   Port: 5434"
    echo "   Database: ui_ai_agent"
    echo "   Username: postgres"
    echo "   Password: postgres"
    echo ""
    echo "📈 pgAdmin Access:"
    echo "   URL: http://localhost:5050"
    echo "   Email: admin@admin.com"
    echo "   Password: admin"
    echo ""
    echo "To stop the database: ./stop-database.sh"
else
    echo "❌ Failed to start database services"
    docker compose logs
    exit 1
fi 