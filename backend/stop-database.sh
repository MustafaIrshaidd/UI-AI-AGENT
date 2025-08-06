#!/bin/bash

echo "🛑 Stopping Database Services..."

# Stop PostgreSQL and pgAdmin
echo "📦 Stopping containers..."
cd .. && docker compose down && cd backend

echo "✅ Database services stopped"
echo ""
echo "To start again: ./start-database.sh" 