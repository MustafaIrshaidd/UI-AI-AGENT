#!/bin/bash

# Script to switch between development and production environments

set -e

FRONTEND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "🔧 Environment Switcher for UI AI Agent Frontend"
echo "================================================"

if [ "$1" = "production" ]; then
    echo "🔄 Switching to PRODUCTION environment..."
    cp "$FRONTEND_DIR/.env.production" "$FRONTEND_DIR/.env"
    echo "✅ Switched to production environment"
    echo "📡 API URL: https://ui-ai-agent.onrender.com"
elif [ "$1" = "development" ]; then
    echo "🔄 Switching to DEVELOPMENT environment..."
    cp "$FRONTEND_DIR/.env.backup" "$FRONTEND_DIR/.env" 2>/dev/null || {
        echo "📝 Creating development environment file..."
        cat > "$FRONTEND_DIR/.env" << 'EOF'
# Development environment
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ENVIRONMENT=development
EOF
    }
    echo "✅ Switched to development environment"
    echo "📡 API URL: http://localhost:8000"
else
    echo "❌ Usage: $0 [development|production]"
    echo ""
    echo "Examples:"
    echo "  $0 development  # Switch to local development"
    echo "  $0 production   # Switch to production deployment"
    exit 1
fi

echo ""
echo "🔄 Restart your development server to apply changes:"
echo "   npm run dev" 