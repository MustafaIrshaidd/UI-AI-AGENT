#!/bin/bash

echo "🛑 Stopping Database Services..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "ℹ️  Docker is not running"
    exit 0
fi

# Check if containers are running
if cd .. && docker compose ps | grep -q "ui_ai_agent_postgres"; then
    echo "📦 Stopping PostgreSQL and pgAdmin containers..."
    if docker compose down; then
        echo "✅ Database services stopped"
    else
        echo "⚠️  Some containers may still be running"
        echo "💡 You can manually stop them with: docker compose down --remove-orphans"
    fi
else
    echo "ℹ️  Database containers are not running"
fi

cd backend

echo ""
echo "To start again: ./scripts/start-database.sh" 