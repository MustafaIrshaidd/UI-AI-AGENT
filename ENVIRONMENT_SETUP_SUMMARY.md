# Environment Setup Summary

This document provides a complete overview of the environment configuration for the UI AI Agent project, ensuring seamless operation between local development and production deployment.

## 🎯 Overview

The project is configured to automatically switch between:
- **Local Development**: Frontend connects to `http://localhost:8000` (local backend)
- **Production**: Frontend connects to your deployed backend (e.g., `https://your-backend.onrender.com`)

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│   (PostgreSQL)  │
│                 │    │                 │    │                 │
│ Local: 3000     │    │ Local: 8000     │    │ Local: 5434     │
│ Prod: Vercel    │    │ Prod: Render    │    │ Prod: Render    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔧 Frontend Configuration

### Environment Variables

| Variable | Development | Production | Description |
|----------|-------------|------------|-------------|
| `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | `https://your-backend.onrender.com` | Backend API URL |
| `NEXT_PUBLIC_ENVIRONMENT` | `development` | `production` | Environment identifier |

### Files Created/Modified

1. **`frontend/src/config/environment.ts`** - Environment configuration logic
2. **`frontend/src/lib/api.ts`** - API client with automatic URL switching
3. **`frontend/next.config.ts`** - Next.js configuration with environment variables
4. **`frontend/components/ApiTest/ApiTest.tsx`** - Testing component
5. **`frontend/scripts/setup-env.sh`** - Setup automation script

### Quick Setup

```bash
# Navigate to frontend directory
cd frontend

# Run setup script
./scripts/setup-env.sh

# Or manually create .env.local
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
echo "NEXT_PUBLIC_ENVIRONMENT=development" >> .env.local
```

## 🔧 Backend Configuration

### Environment Variables

| Variable | Development | Production | Description |
|----------|-------------|------------|-------------|
| `ENVIRONMENT` | `development` | `production` | Environment identifier |
| `FRONTEND_URL` | `http://localhost:3000` | `https://your-frontend-domain.com` | Frontend URL for CORS |

### Files Created/Modified

1. **`backend/src/core/config/development.py`** - Development configuration
2. **`backend/src/core/config/production.py`** - Production configuration (updated)
3. **`backend/main.py`** - Environment-aware configuration loading

### CORS Configuration

The backend automatically configures CORS based on environment:

- **Development**: Allows localhost origins (3000, 3001, 3002)
- **Production**: Allows only production frontend domains

## 🚀 Deployment Workflow

### 1. Local Development

```bash
# Terminal 1: Start backend
cd backend
python main.py

# Terminal 2: Start frontend
cd frontend
npm run dev
```

### 2. Production Deployment

#### Backend (Render)
1. Deploy to Render
2. Set environment variables:
   ```
   ENVIRONMENT=production
   FRONTEND_URL=https://your-frontend-domain.com
   ```

#### Frontend (Vercel/Netlify)
1. Deploy to your platform
2. Set environment variables:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
   NEXT_PUBLIC_ENVIRONMENT=production
   ```

## 🧪 Testing

### API Test Component

The frontend includes a built-in test component that:
- Shows current environment configuration
- Tests API connectivity
- Displays CORS configuration
- Provides debugging information

### Manual Testing

```bash
# Test backend health
curl http://localhost:8000/health

# Test CORS configuration
curl http://localhost:8000/cors-config

# Test frontend environment
curl http://localhost:3000
```

## 🔍 Troubleshooting

### Common Issues

1. **CORS Errors**
   - Check that frontend URL is in backend's allowed origins
   - Verify environment variables are set correctly
   - Restart both services after changes

2. **API Connection Failed**
   - Verify backend is running
   - Check API URL in frontend configuration
   - Ensure network connectivity

3. **Environment Variables Not Loading**
   - Restart development server after adding `.env.local`
   - Check variable names (must start with `NEXT_PUBLIC_` for client-side)
   - Verify file location (must be in frontend root)

### Debug Commands

```bash
# Check frontend environment
cd frontend && npm run dev

# Check backend environment
cd backend && python main.py

# Test API directly
curl -X GET http://localhost:8000/health
```

## 📋 Checklist

### Local Development
- [ ] Backend running on `http://localhost:8000`
- [ ] Frontend running on `http://localhost:3000`
- [ ] `.env.local` file created in frontend directory
- [ ] API Test component shows successful connection
- [ ] No CORS errors in browser console

### Production Deployment
- [ ] Backend deployed to Render with correct environment variables
- [ ] Frontend deployed to Vercel/Netlify with correct environment variables
- [ ] Production domains added to backend CORS configuration
- [ ] SSL certificates configured (if needed)
- [ ] Environment variables set in deployment platform

## 📚 Additional Resources

- [Frontend Environment Setup](./frontend/ENVIRONMENT_SETUP.md)
- [Frontend README](./frontend/README.md)
- [Backend Configuration Files](./backend/src/core/config/)
- [API Client Documentation](./frontend/src/lib/api.ts)

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review the API Test component output
3. Check browser developer tools for errors
4. Verify all environment variables are set correctly
5. Ensure both frontend and backend are running

The setup is designed to be robust and provide clear feedback when something goes wrong. The API Test component will help you identify and resolve most common issues. 