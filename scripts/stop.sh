#!/bin/bash

echo "🛑 Stopping UI AI Agent services..."

# Function to check if a process is running
is_process_running() {
    pgrep -f "$1" > /dev/null
}

# Function to kill process by pattern
kill_process() {
    local pattern="$1"
    local process_name="$2"
    
    if is_process_running "$pattern"; then
        echo "🔄 Stopping $process_name..."
        pkill -f "$pattern"
        
        # Wait for process to stop
        local attempts=0
        while is_process_running "$pattern" && [ $attempts -lt 10 ]; do
            sleep 1
            attempts=$((attempts + 1))
        done
        
        if is_process_running "$pattern"; then
            echo "⚠️  Force killing $process_name..."
            pkill -9 -f "$pattern"
        else
            echo "✅ $process_name stopped"
        fi
    else
        echo "ℹ️  $process_name is not running"
    fi
}

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "ℹ️  Docker is not running"
else
    # Stop Docker containers
    echo "🔄 Stopping Docker containers..."
    if docker compose down; then
        echo "✅ Docker containers stopped"
    else
        echo "⚠️  Some Docker containers may still be running"
    fi
fi

# Kill backend processes
kill_process "uvicorn main:app" "FastAPI backend"

# Kill frontend processes
kill_process "next dev" "Next.js frontend"

# Additional cleanup for any remaining processes
echo "🧹 Cleaning up any remaining processes..."

# Kill any remaining Python processes from this project
if is_process_running "python.*main:app"; then
    echo "🔄 Stopping remaining Python processes..."
    pkill -f "python.*main:app"
fi

# Kill any remaining Node processes from this project
if is_process_running "node.*next"; then
    echo "🔄 Stopping remaining Node processes..."
    pkill -f "node.*next"
fi

echo ""
echo "✅ All services stopped!"
echo ""
echo "To start again: ./scripts/start.sh" 