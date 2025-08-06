#!/bin/bash

echo "🔄 Resetting Database..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Stop and remove containers with volumes
echo "📦 Stopping and removing containers..."
cd .. && docker compose down -v && cd backend

# Start fresh
echo "🐘 Starting fresh database..."
cd .. && docker compose up -d && cd backend

echo "⏳ Waiting for database to be ready..."
sleep 10

# Check if services are running
if cd .. && docker compose ps | grep -q "ui_ai_agent_postgres.*Up"; then
    cd backend
    echo "✅ Database reset complete!"
    echo "📊 Fresh database is running on localhost:5434"
    echo "📈 pgAdmin is available at http://localhost:5050"
    echo ""
    echo "Sample data has been loaded:"
    echo "   - 2 users (john.doe@example.com, jane.smith@example.com)"
    echo "   - 3 jobs (Senior Python Developer, Frontend React Developer, DevOps Engineer)"
else
    echo "❌ Failed to reset database"
    docker compose logs
    exit 1
fi 