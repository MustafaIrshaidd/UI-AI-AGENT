# Frontend Scripts

This directory contains scripts for managing the frontend environment and configuration.

## 🌍 Environment Management Scripts

### `setup-env.sh`
Sets up the frontend environment configuration.

**Usage:**
```bash
./scripts/setup-env.sh
```

**What it does:**
- Creates `.env.local` file for development
- Sets up environment variables
- Configures API endpoints
- Validates configuration

### `switch-env.sh`
Switches between development and production environments.

**Usage:**
```bash
# Switch to development
./scripts/switch-env.sh dev

# Switch to production
./scripts/switch-env.sh prod
```

**What it does:**
- Updates environment variables
- Switches API endpoints
- Configures CORS settings
- Updates build configuration

## 🔧 Environment Variables

### Development (`.env.local`)
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ENVIRONMENT=development
```

### Production (`.env.production`)
```bash
NEXT_PUBLIC_API_URL=https://ui-ai-agent.onrender.com
NEXT_PUBLIC_ENVIRONMENT=production
```

## 📋 Quick Commands

```bash
# Setup environment
./scripts/setup-env.sh

# Switch to development
./scripts/switch-env.sh dev

# Switch to production
./scripts/switch-env.sh prod

# Start development server
npm run dev

# Build for production
npm run build
```

## 🔍 Troubleshooting

### Environment Issues
- Restart development server after environment changes
- Clear browser cache if changes don't appear
- Check `.env.local` file exists and has correct values

### API Connection Issues
- Verify backend is running on correct port
- Check CORS configuration
- Ensure environment variables are set correctly

## 📡 Available Endpoints

| Environment | Backend URL | Status |
|-------------|-------------|--------|
| Development | `http://localhost:8000` | Local |
| Production | `https://ui-ai-agent.onrender.com` | Render | 