#!/bin/bash

echo "🚀 Production Database Migration Script for UI AI Agent Backend"

# Exit on any error
set -e

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this script from the backend directory."
    exit 1
fi

# Check if Poetry is available
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not available. Please install Poetry first."
    exit 1
fi

# Check if Alembic is available
if ! poetry run alembic --version &> /dev/null; then
    echo "❌ Alembic is not available. Installing dependencies..."
    poetry install --no-dev
fi

# Function to check database connection
check_db_connection() {
    echo "🔍 Checking database connection..."
    
    # Test database connection with retries
    local max_attempts=5
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        echo "Attempt $attempt/$max_attempts to connect to database..."
        
        if poetry run python -c "
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
            echo "✅ Database connection successful!"
            return 0
        else
            echo "❌ Database connection failed (attempt $attempt/$max_attempts)"
            if [ $attempt -lt $max_attempts ]; then
                echo "⏳ Waiting 10 seconds before retry..."
                sleep 10
            fi
            attempt=$((attempt + 1))
        fi
    done
    
    echo "❌ Failed to connect to database after $max_attempts attempts"
    exit 1
}

# Function to check if migrations are needed
check_migrations_needed() {
    echo "🔍 Checking if migrations are needed..."
    
    local current_rev=$(poetry run alembic current 2>/dev/null | head -n1 | awk '{print $1}' || echo "none")
    local head_rev=$(poetry run alembic heads 2>/dev/null | head -n1 | awk '{print $1}' || echo "none")
    
    if [ "$current_rev" = "$head_rev" ]; then
        echo "✅ Database is up to date. No migrations needed."
        return 0
    else
        echo "📋 Migrations needed:"
        echo "   Current revision: $current_rev"
        echo "   Head revision: $head_rev"
        return 1
    fi
}

# Function to apply migrations safely
apply_migrations() {
    echo "🚀 Applying database migrations..."
    
    # Show current status
    echo "📊 Current migration status:"
    poetry run alembic current
    
    # Show pending migrations
    echo "📋 Pending migrations:"
    poetry run alembic show "$(poetry run alembic heads | head -n1 | awk '{print $1}')"
    
    # Apply migrations
    poetry run alembic upgrade head
    
    if [ $? -eq 0 ]; then
        echo "✅ All migrations applied successfully!"
        
        # Show new status
        echo "📊 New migration status:"
        poetry run alembic current
    else
        echo "❌ Failed to apply migrations"
        exit 1
    fi
}

# Function to verify migration success
verify_migration() {
    echo "🔍 Verifying migration success..."
    
    # Check if we can connect and query the database
    if poetry run python -c "
import os
from src.core.config.database import engine
from sqlalchemy import text
try:
    with engine.connect() as conn:
        # Test a simple query
        result = conn.execute(text('SELECT COUNT(*) FROM alembic_version'))
        version_count = result.scalar()
        print(f'✅ Migration verification successful. Version count: {version_count}')
except Exception as e:
    print(f'❌ Migration verification failed: {e}')
    exit(1)
" 2>/dev/null; then
        echo "✅ Migration verification successful!"
    else
        echo "❌ Migration verification failed"
        exit 1
    fi
}

# Main execution
echo "🚀 Starting production database migration process..."

# Check database connection
check_db_connection

# Check if migrations are needed
if check_migrations_needed; then
    echo "✅ No migrations needed. Exiting successfully."
    exit 0
fi

# Apply migrations
apply_migrations

# Verify migration success
verify_migration

echo "🎉 Production database migration completed successfully!" 