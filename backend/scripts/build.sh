#!/bin/bash

# Build script for Render deployment

set -e

echo "🔧 Starting build process..."

# Install Poetry if not already installed
if ! command -v poetry &> /dev/null; then
    echo "📦 Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Configure Poetry
echo "⚙️ Configuring Poetry..."
poetry config virtualenvs.create false

# Install dependencies
echo "📚 Installing dependencies..."
poetry install --only=main --no-root

# Run database migrations (if needed)
echo "🗄️ Setting up database..."
# poetry run alembic upgrade head

echo "✅ Build completed successfully!" 