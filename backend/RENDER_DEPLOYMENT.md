# Render Deployment Guide

This guide explains how to deploy the UI AI Agent backend to Render.

## 🚀 Quick Deploy

### Option 1: Using render.yaml (Recommended)

1. **Push your code to GitHub**
2. **Connect your repository to Render**
3. **Render will automatically detect the `render.yaml` file**
4. **Deploy with one click**

### Option 2: Manual Configuration

1. **Create a new Web Service on Render**
2. **Connect your GitHub repository**
3. **Configure the following settings:**

#### Build Settings
- **Build Command**: `pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev`
- **Start Command**: `poetry run uvicorn main:app --host 0.0.0.0 --port $PORT`

#### Environment Variables
```
ENVIRONMENT=production
PYTHON_VERSION=3.13.0
DATABASE_URL=<your-postgresql-connection-string>
FRONTEND_URL=https://your-frontend-domain.com
```

## 🗄️ Database Setup

### Option 1: Render PostgreSQL (Recommended)

1. **Create a new PostgreSQL database on Render**
2. **Copy the connection string**
3. **Set it as `DATABASE_URL` environment variable**

### Option 2: External Database

Use any PostgreSQL database and set the connection string as `DATABASE_URL`.

## 🔧 Configuration Files

### render.yaml
```yaml
services:
  - type: web
    name: ui-ai-agent-backend
    env: python
    plan: free
    buildCommand: |
      pip install poetry
      poetry config virtualenvs.create false
      poetry install --no-dev
    startCommand: poetry run uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Dockerfile (Alternative)
If you prefer Docker deployment:
```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🌐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ENVIRONMENT` | Environment name | Yes |
| `DATABASE_URL` | PostgreSQL connection string | Yes |
| `FRONTEND_URL` | Frontend URL for CORS | Yes |
| `PYTHON_VERSION` | Python version | No |

## 📊 Health Checks

The application includes health check endpoints:
- `/health` - Basic health status
- `/cors-config` - CORS configuration info

## 🔍 Troubleshooting

### Common Issues

1. **Poetry not found**
   - Solution: Use the build command with Poetry installation

2. **Database connection failed**
   - Check `DATABASE_URL` environment variable
   - Ensure database is accessible from Render

3. **Port binding issues**
   - Use `$PORT` environment variable in start command
   - Render automatically provides this

4. **Dependencies not found**
   - Ensure all dependencies are in `pyproject.toml`
   - Use `poetry install --no-dev` for production

### Logs

Check Render logs for detailed error information:
1. Go to your service dashboard
2. Click on "Logs" tab
3. Look for build or runtime errors

## 🚀 Post-Deployment

After successful deployment:

1. **Test the health endpoint**: `https://your-app.onrender.com/health`
2. **Test GraphQL playground**: `https://your-app.onrender.com/graphql`
3. **Update frontend environment**: Set `NEXT_PUBLIC_API_URL` to your Render URL

## 📈 Monitoring

- **Health checks**: Automatic monitoring via `/health` endpoint
- **Logs**: Available in Render dashboard
- **Metrics**: Basic metrics in Render dashboard

## 🔐 Security

- Environment variables are encrypted
- HTTPS is automatically enabled
- CORS is configured for your frontend domain 