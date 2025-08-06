#!/bin/bash

echo "🐘 Starting Database Services..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Start PostgreSQL and pgAdmin
echo "📦 Starting PostgreSQL and pgAdmin..."
cd .. && docker compose up -d && cd backend

echo "⏳ Waiting for services to be ready..."
sleep 5

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