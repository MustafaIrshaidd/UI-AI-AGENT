#!/bin/bash

echo "🛑 Stopping all UI AI Agent services..."

# Stop processes on ports 8000 and 3000
if command -v lsof >/dev/null 2>&1; then
    echo "🔄 Stopping backend processes on port 8000..."
    BACKEND_PIDS=$(lsof -ti tcp:8000)
    if [ -n "$BACKEND_PIDS" ]; then
        echo "   Found processes: $BACKEND_PIDS"
        kill $BACKEND_PIDS 2>/dev/null || true
        sleep 2
        
        # Force kill if still running
        BACKEND_PIDS=$(lsof -ti tcp:8000)
        if [ -n "$BACKEND_PIDS" ]; then
            echo "   Force stopping backend processes..."
            kill -9 $BACKEND_PIDS 2>/dev/null || true
        fi
    else
        echo "   No backend processes found on port 8000"
    fi
    
    echo "🔄 Stopping frontend processes on port 3000..."
    FRONTEND_PIDS=$(lsof -ti tcp:3000)
    if [ -n "$FRONTEND_PIDS" ]; then
        echo "   Found processes: $FRONTEND_PIDS"
        kill $FRONTEND_PIDS 2>/dev/null || true
        sleep 2
        
        # Force kill if still running
        FRONTEND_PIDS=$(lsof -ti tcp:3000)
        if [ -n "$FRONTEND_PIDS" ]; then
            echo "   Force stopping frontend processes..."
            kill -9 $FRONTEND_PIDS 2>/dev/null || true
        fi
    else
        echo "   No frontend processes found on port 3000"
    fi
fi

# Stop Docker containers
echo "🔄 Stopping Docker containers..."
cd backend && cd .. && docker compose down

echo "✅ All services stopped!"
echo ""
echo "💡 Note: If you have terminal windows open for backend/frontend,"
echo "   you may need to close them manually or they will show connection errors." 