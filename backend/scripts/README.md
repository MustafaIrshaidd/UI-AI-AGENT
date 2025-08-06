# Backend Scripts

This directory contains scripts for managing the backend services.

## 🗄️ Database Scripts

### `start-database.sh`
Starts PostgreSQL database using Docker Compose with health monitoring.

**Usage:**
```bash
./scripts/start-database.sh
```

**What it does:**
- ✅ Checks Docker availability
- ✅ Verifies Docker Compose
- ✅ Stops existing containers for clean start
- ✅ Starts PostgreSQL container
- ✅ Starts pgAdmin container
- ✅ Monitors database health with retry logic
- ✅ Provides detailed status information

### `stop-database.sh`
Stops the PostgreSQL database and pgAdmin with status verification.

**Usage:**
```bash
./scripts/stop-database.sh
```

**What it does:**
- ✅ Checks Docker availability
- ✅ Verifies container status
- ✅ Gracefully stops containers
- ✅ Provides helpful error messages

### `reset-database.sh`
Resets the database and runs migrations.

**Usage:**
```bash
./scripts/reset-database.sh
```

**What it does:**
- Stops existing database
- Removes old data
- Starts fresh database
- Runs initialization scripts

## 🔥 Development Scripts

### `start-backend.sh`
Starts the FastAPI development server with Docker integration.

**Usage:**
```bash
./scripts/start-backend.sh
```

**What it does:**
- ✅ Checks Docker availability
- ✅ Verifies Docker Compose
- ✅ Starts database if not running
- ✅ Monitors database health
- ✅ Installs Python dependencies with Poetry
- ✅ Sets environment variables
- ✅ Starts uvicorn server with hot reload
- ✅ Runs on http://localhost:8000

### `build.sh`
Builds the Docker image for deployment.

**Usage:**
```bash
./scripts/build.sh
```

**What it does:**
- Builds Docker image
- Tags it appropriately
- Prepares for deployment

## 🔧 Environment Variables

These scripts use the following environment variables:

```bash
DATABASE_URL=postgresql://postgres:postgres@localhost:5434/ui_ai_agent
FRONTEND_URL=http://localhost:3000
ENVIRONMENT=development
DEBUG=true
```

## 📋 Quick Commands

```bash
# Start database only
./scripts/start-database.sh

# Start backend only
./scripts/start-backend.sh

# Reset database
./scripts/reset-database.sh

# Stop database
./scripts/stop-database.sh

# Build for deployment
./scripts/build.sh
```

## 🔍 Troubleshooting

### Database Issues
- Ensure Docker is running
- Check if port 5434 is available
- Verify Docker Compose configuration

### Backend Issues
- Make sure Poetry is installed
- Check Python version compatibility
- Verify all dependencies are installed 