#!/bin/bash

echo "🗄️  Database Migration Script for UI AI Agent Backend"

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this script from the backend directory."
    exit 1
fi

# Check if Poetry is available
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not available. Please install Poetry first."
    echo "💡 Install with: curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

# Check if Alembic is available
if ! poetry run alembic --version &> /dev/null; then
    echo "❌ Alembic is not available. Installing dependencies..."
    poetry install
fi

# Function to check database connection
check_db_connection() {
    echo "🔍 Checking database connection..."
    
    # Check if POSTGRES_PASSWORD is set
    if [ -z "$POSTGRES_PASSWORD" ]; then
        echo "❌ POSTGRES_PASSWORD environment variable is not set."
        echo "💡 Set it with: export POSTGRES_PASSWORD=your_password"
        echo "💡 Or add it to your .env file"
        exit 1
    fi
    
    # Test database connection
    if ! poetry run python -c "
import os
from src.core.config.database import engine
from sqlalchemy import text
try:
    with engine.connect() as conn:
        conn.execute(text('SELECT 1'))
    print('✅ Database connection successful')
except Exception as e:
    print(f'❌ Database connection failed: {e}')
    exit(1)
" 2>/dev/null; then
        echo "❌ Cannot connect to database. Please check:"
        echo "   1. Database is running (docker compose up -d)"
        echo "   2. POSTGRES_PASSWORD is correct"
        echo "   3. Database URL is properly configured"
        exit 1
    fi
}

# Function to create new migration
create_migration() {
    local message="$1"
    if [ -z "$message" ]; then
        read -p "Enter migration description: " message
    fi
    
    echo "📝 Creating new migration: $message"
    poetry run alembic revision --autogenerate -m "$message"
    
    if [ $? -eq 0 ]; then
        echo "✅ Migration created successfully!"
        echo "💡 Review the generated migration file in alembic/versions/"
        echo "💡 Apply it with: poetry run alembic upgrade head"
    else
        echo "❌ Failed to create migration"
        exit 1
    fi
}

# Function to apply migrations
apply_migrations() {
    echo "🚀 Applying database migrations..."
    poetry run alembic upgrade head
    
    if [ $? -eq 0 ]; then
        echo "✅ All migrations applied successfully!"
    else
        echo "❌ Failed to apply migrations"
        exit 1
    fi
}

# Function to show migration status
show_status() {
    echo "📊 Migration Status:"
    poetry run alembic current
    echo ""
    echo "📋 Migration History:"
    poetry run alembic history --verbose
}

# Function to rollback migration
rollback_migration() {
    local revision="$1"
    if [ -z "$revision" ]; then
        echo "📋 Available revisions:"
        poetry run alembic history --verbose
        echo ""
        read -p "Enter revision ID to rollback to: " revision
    fi
    
    echo "⏪ Rolling back to revision: $revision"
    poetry run alembic downgrade "$revision"
    
    if [ $? -eq 0 ]; then
        echo "✅ Rollback successful!"
    else
        echo "❌ Rollback failed"
        exit 1
    fi
}

# Main script logic
case "${1:-}" in
    "create")
        check_db_connection
        create_migration "$2"
        ;;
    "apply"|"upgrade")
        check_db_connection
        apply_migrations
        ;;
    "status")
        show_status
        ;;
    "rollback"|"downgrade")
        check_db_connection
        rollback_migration "$2"
        ;;
    "init")
        echo "🔧 Initializing database with current models..."
        check_db_connection
        echo "📝 Creating initial migration..."
        poetry run alembic revision --autogenerate -m "Initial migration"
        echo "🚀 Applying migration..."
        poetry run alembic upgrade head
        echo "✅ Database initialized successfully!"
        ;;
    "help"|"-h"|"--help"|"")
        echo "🗄️  Database Migration Script"
        echo ""
        echo "Usage: $0 [command] [options]"
        echo ""
        echo "Commands:"
        echo "  create [message]  Create a new migration with optional message"
        echo "  apply|upgrade     Apply all pending migrations"
        echo "  status           Show current migration status and history"
        echo "  rollback [rev]   Rollback to specific revision"
        echo "  init             Initialize database with current models"
        echo "  help             Show this help message"
        echo ""
        echo "Examples:"
        echo "  $0 create 'Add user profile fields'"
        echo "  $0 apply"
        echo "  $0 status"
        echo "  $0 rollback abc123"
        echo "  $0 init"
        echo ""
        echo "Environment Variables:"
        echo "  POSTGRES_PASSWORD  Database password (required)"
        echo ""
        echo "💡 Make sure your database is running: docker compose up -d"
        ;;
    *)
        echo "❌ Unknown command: $1"
        echo "💡 Use '$0 help' for usage information"
        exit 1
        ;;
esac 