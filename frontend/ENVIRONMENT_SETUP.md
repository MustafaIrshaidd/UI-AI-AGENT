# Frontend Environment Setup

This document explains how to configure the frontend to work with different backend environments.

## 🚀 Quick Start

### Development (Local)
```bash
# Switch to development environment
npm run env:dev

# Start development server
npm run dev
```

### Production (Deploy)
```bash
# Switch to production environment
npm run env:prod

# Build for production
npm run build
npm run start
```

## 📁 Environment Files

### `.env` (Development - Default)
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ENVIRONMENT=development
```

### `.env.production` (Production)
```bash
NEXT_PUBLIC_API_URL=https://ui-ai-agent.onrender.com
NEXT_PUBLIC_ENVIRONMENT=production
```

## 🔧 Available Scripts

| Script | Description |
|--------|-------------|
| `npm run env:dev` | Switch to development environment |
| `npm run env:prod` | Switch to production environment |
| `npm run env:status` | Show current API URL |
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run start` | Start production server |

## 🌐 Environment Detection

The frontend automatically detects the environment and configures:

- **API URL**: Points to localhost:8000 in development, Render URL in production
- **CORS**: Configured for cross-origin requests
- **Logging**: Enhanced logging in development mode
- **Security**: Production-specific security headers

## 🔍 Visual Indicators

In development mode, you'll see:
- Environment status indicator in bottom-right corner
- Console logs showing current configuration
- API URL displayed in the UI

## 🚨 Troubleshooting

### API Connection Issues
1. Check if backend is running: `http://localhost:8000/health`
2. Verify environment: `npm run env:status`
3. Check browser console for configuration logs

### Environment Not Updating
1. Restart the development server after switching environments
2. Clear browser cache
3. Check `.env` file contents

## 📡 Backend URLs

| Environment | Backend URL | Status |
|-------------|-------------|--------|
| Development | `http://localhost:8000` | Local |
| Production | `https://ui-ai-agent.onrender.com` | Render |

## 🔐 Security Notes

- Environment variables prefixed with `NEXT_PUBLIC_` are exposed to the client
- Production builds include additional security headers
- CORS is configured for both environments

## Backend Configuration

### Local Development

Set these environment variables for your backend:

```bash
ENVIRONMENT=development
FRONTEND_URL=http://localhost:3000
```

### Production (Render)

Set these environment variables in your Render service:

```bash
ENVIRONMENT=production
FRONTEND_URL=https://your-frontend-domain.com
```

## Testing the Configuration

1. Start your backend: `cd backend && python main.py`
2. Start your frontend: `cd frontend && npm run dev`
3. Open http://localhost:3000
4. Visit `/test-config` to verify your configuration
5. Check browser console for environment logs

## Environment Variable Reference

| Variable | Description | Development | Production |
|----------|-------------|-------------|------------|
| `NEXT_PUBLIC_API_URL` | Backend API URL | `http://localhost:8000` | `https://ui-ai-agent.onrender.com` |
| `NEXT_PUBLIC_ENVIRONMENT` | Environment name | `development` | `production` |
| `ENVIRONMENT` | Backend environment | `development` | `production` |
| `FRONTEND_URL` | Frontend URL for CORS | `http://localhost:3000` | `https://your-frontend-domain.com` |
