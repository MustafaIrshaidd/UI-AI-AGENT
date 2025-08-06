# Scripts Directory

This directory contains all the utility scripts for managing the UI AI Agent project.

## 🚀 Project Management Scripts

### `start.sh`
Starts the entire application stack:
- PostgreSQL database with Docker (with health checks)
- FastAPI backend server (with connection verification)
- Next.js frontend development server (with status check)

**Usage:**
```bash
./scripts/start.sh
```

**Features:**
- ✅ Docker availability check
- ✅ Docker Compose verification
- ✅ PostgreSQL health monitoring
- ✅ Service status verification
- ✅ Graceful shutdown with Ctrl+C
- ✅ Automatic cleanup on exit

**Services started:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- GraphQL: http://localhost:8000/graphql
- API Docs: http://localhost:8000/docs
- pgAdmin: http://localhost:5050

### `stop.sh`
Stops all running services and cleans up:
- Kills backend and frontend processes (with graceful shutdown)
- Stops Docker containers (with status verification)
- Cleans up any remaining processes

**Usage:**
```bash
./scripts/stop.sh
```

**Features:**
- ✅ Process status checking
- ✅ Graceful shutdown with retry
- ✅ Force kill for stubborn processes
- ✅ Docker container verification
- ✅ Comprehensive cleanup

## 🔧 Backend Scripts

Located in `backend/scripts/`:

### Database Management
- `start-database.sh` - Start PostgreSQL database with Docker
- `stop-database.sh` - Stop PostgreSQL database
- `reset-database.sh` - Reset database and run migrations

### Development
- `start-backend.sh` - Start FastAPI development server
- `build.sh` - Build Docker image for deployment

## 🎨 Frontend Scripts

Located in `frontend/scripts/`:

### Environment Management
- `setup-env.sh` - Setup environment configuration
- `switch-env.sh` - Switch between development and production environments

## 📋 Quick Commands

```bash
# Start everything
./scripts/start.sh

# Stop everything
./scripts/stop.sh

# Start only backend
cd backend && ./scripts/start-backend.sh

# Start only database
cd backend && ./scripts/start-database.sh

# Setup frontend environment
cd frontend && ./scripts/setup-env.sh
```

## 🔍 Troubleshooting

If scripts fail to execute:
1. Make sure they have execute permissions: `chmod +x scripts/*.sh`
2. Ensure Docker is running for database scripts
3. Check that all dependencies are installed 