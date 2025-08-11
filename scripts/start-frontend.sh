#!/bin/bash

echo "🎨 Starting UI AI Agent Frontend..."

# Check if we're in the right directory
if [ ! -f "frontend/package.json" ]; then
    echo "❌ Error: frontend/package.json not found. Please run this script from the project root directory."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node >/dev/null 2>&1; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    echo "💡 You can download it from: https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm >/dev/null 2>&1; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

# Ensure required ports are free before starting
if command -v lsof >/dev/null 2>&1; then
    echo "🧹 Ensuring port 3000 is free..."
    PIDS=$(lsof -ti tcp:3000)
    if [ -n "$PIDS" ]; then
        echo "⚠️  Port 3000 is in use by PID(s): $PIDS — attempting to free..."
        kill $PIDS 2>/dev/null || true
        sleep 1
        PIDS=$(lsof -ti tcp:3000)
        if [ -n "$PIDS" ]; then
            echo "⚠️  Force killing PID(s) on port 3000: $PIDS"
            kill -9 $PIDS 2>/dev/null || true
        fi
    fi
fi

# Go to frontend directory
cd frontend

# Install frontend dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
fi

echo ""
echo "🚀 Starting Next.js development server..."
echo "🌐 Frontend URL: http://localhost:3000"
echo "📱 Profile Page: http://localhost:3000/profile"
echo ""
echo "Press Ctrl+C to stop the frontend server"
echo ""

# Start the development server
npm run dev 