# Backend Scripts

This directory contains essential scripts for managing the backend services.

## 🗄️ Database Migration Script

### `migrate-db.sh`
Comprehensive database migration management script using Alembic.

**Usage:**
```bash
./scripts/migrate-db.sh [command] [options]
```

**Commands:**
- `create [message]` - Create a new migration with optional message
- `apply|upgrade` - Apply all pending migrations
- `status` - Show current migration status and history
- `rollback [rev]` - Rollback to specific revision
- `init` - Initialize database with current models
- `help` - Show help message

**Examples:**
```bash
# Create a new migration
./scripts/migrate-db.sh create 'Add user profile fields'

# Apply all migrations
./scripts/migrate-db.sh apply

# Check migration status
./scripts/migrate-db.sh status

# Initialize database
./scripts/migrate-db.sh init
```

**What it does:**
- ✅ Checks Poetry and Alembic availability
- ✅ Verifies database connection
- ✅ Creates and applies migrations
- ✅ Provides rollback functionality
- ✅ Shows migration history and status

## 🚀 Development Script

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

## 🔧 Environment Variables

These scripts use the following environment variables:

```bash
POSTGRES_PASSWORD=your_secure_password
DATABASE_URL=postgresql://postgres:your_password@localhost:5434/ui_ai_agent
FRONTEND_URL=http://localhost:3000
ENVIRONMENT=development
DEBUG=true
```

## 📋 Quick Commands

```bash
# Start backend (includes database startup)
./scripts/start-backend.sh

# Database migrations
./scripts/migrate-db.sh init      # Initialize database
./scripts/migrate-db.sh create    # Create new migration
./scripts/migrate-db.sh apply     # Apply migrations
./scripts/migrate-db.sh status    # Check status
```

## 🔍 Troubleshooting

### Database Issues
- Ensure Docker is running
- Check if port 5434 is available
- Verify Docker Compose configuration
- Set POSTGRES_PASSWORD environment variable

### Backend Issues
- Make sure Poetry is installed
- Check Python version compatibility
- Verify all dependencies are installed

### Migration Issues
- Ensure database is running and accessible
- Check POSTGRES_PASSWORD is set correctly
- Verify models are properly imported in database.py 