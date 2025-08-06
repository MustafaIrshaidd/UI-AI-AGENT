#!/bin/bash

echo "🛑 Stopping UI AI Agent services..."

# Kill backend process
echo "🔄 Stopping FastAPI backend..."
pkill -f "uvicorn main:app"

# Kill frontend process
echo "🔄 Stopping Next.js frontend..."
pkill -f "next dev"

# Stop Docker containers
echo "🔄 Stopping PostgreSQL and pgAdmin..."
docker compose down

echo "✅ All services stopped!"
echo ""
echo "To start again: ./start.sh" 