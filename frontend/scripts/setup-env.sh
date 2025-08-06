#!/bin/bash

# Environment Setup Script for UI AI Agent Frontend

echo "🚀 Setting up environment variables for UI AI Agent Frontend"

# Check if .env.local already exists
if [ -f ".env.local" ]; then
    echo "⚠️  .env.local already exists. Do you want to overwrite it? (y/n)"
    read -r response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        echo "📝 Overwriting .env.local..."
    else
        echo "❌ Setup cancelled."
        exit 0
    fi
fi

# Get backend URL from user
echo "🔧 Please enter your backend URL:"
echo "   - For local development: http://localhost:8000"
echo "   - For production: https://your-backend.onrender.com"
read -p "Backend URL: " backend_url

# Validate URL format
if [[ ! $backend_url =~ ^https?:// ]]; then
    echo "❌ Invalid URL format. Please include http:// or https://"
    exit 1
fi

# Determine environment based on URL
if [[ $backend_url == *"localhost"* ]] || [[ $backend_url == *"127.0.0.1"* ]]; then
    environment="development"
    echo "🔍 Detected development environment"
else
    environment="production"
    echo "🔍 Detected production environment"
fi

# Create .env.local file
cat > .env.local << EOF
# Environment Configuration for UI AI Agent Frontend
# Generated on $(date)

# API Configuration
NEXT_PUBLIC_API_URL=$backend_url
NEXT_PUBLIC_ENVIRONMENT=$environment

# Additional Configuration
# Add any other environment variables you need below
EOF

echo "✅ Environment file created successfully!"
echo "📁 File: .env.local"
echo "🔗 Backend URL: $backend_url"
echo "🌍 Environment: $environment"
echo ""
echo "🚀 Next steps:"
echo "1. Start your backend server"
echo "2. Run 'npm run dev' to start the frontend"
echo "3. Open http://localhost:3000 to test the configuration"
echo ""
echo "📖 For more information, see ENVIRONMENT_SETUP.md" 