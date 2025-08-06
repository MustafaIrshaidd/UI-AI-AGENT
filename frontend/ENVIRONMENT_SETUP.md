# Environment Setup Guide

This guide explains how to configure environment variables for different deployment environments.

## Local Development

Create a `.env.local` file in the frontend directory:

```bash
# Local Development Environment
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ENVIRONMENT=development
```

## Production Deployment

### Vercel Deployment

1. Go to your Vercel project dashboard
2. Navigate to Settings > Environment Variables
3. Add the following variables:

```
NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
NEXT_PUBLIC_ENVIRONMENT=production
```

### Netlify Deployment

1. Go to your Netlify site dashboard
2. Navigate to Site settings > Environment variables
3. Add the following variables:

```
NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
NEXT_PUBLIC_ENVIRONMENT=production
```

### Other Platforms

Set the same environment variables in your deployment platform:

```
NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
NEXT_PUBLIC_ENVIRONMENT=production
```

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
4. The API Test component will show your current configuration
5. Click "Test API Connection" to verify everything works

## Troubleshooting

### CORS Issues

If you encounter CORS errors:

1. Check that your frontend URL is in the backend's allowed origins
2. Verify the environment variables are set correctly
3. Restart both frontend and backend after changing environment variables

### API Connection Issues

1. Verify the API URL is correct
2. Check that the backend is running
3. Ensure the backend is accessible from your frontend's domain

## Environment Variable Reference

| Variable | Description | Development | Production |
|----------|-------------|-------------|------------|
| `NEXT_PUBLIC_API_URL` | Backend API URL | `http://localhost:8000` | `https://your-backend.onrender.com` |
| `NEXT_PUBLIC_ENVIRONMENT` | Environment name | `development` | `production` |
| `ENVIRONMENT` | Backend environment | `development` | `production` |
| `FRONTEND_URL` | Frontend URL for CORS | `http://localhost:3000` | `https://your-frontend-domain.com` | 