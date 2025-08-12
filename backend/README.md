# UI AI Agent Backend

A FastAPI-based backend service with GraphQL support for the UI AI Agent application.

## 🚀 Features

- **FastAPI**: Modern, fast web framework
- **GraphQL**: Flexible API with Strawberry GraphQL
- **PostgreSQL**: Robust database with SQLModel ORM
- **Docker**: Containerized deployment
- **Health Checks**: Built-in monitoring endpoints
- **Automatic Migrations**: Production-ready database migration system

## 🏗️ Architecture

```
backend/
├── src/
│   ├── api/          # API routes and GraphQL
│   ├── core/         # Configuration and core setup
│   ├── models/       # Database models
│   ├── services/     # Business logic
│   └── utils/        # Utility functions
├── tests/            # Test suite
├── main.py           # Application entry point
└── pyproject.toml    # Dependencies and project config
```

## 🛠️ Development

### Prerequisites

- Python 3.13+
- Poetry
- PostgreSQL
- Docker (optional)

### Setup

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Database setup:**
   ```bash
   # Start PostgreSQL
   docker-compose up -d postgres
   
   # Run migrations (using the migration script)
   ./scripts/migrate-db.sh init
   ```

4. **Start development server:**
   ```bash
   poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## 📡 API Endpoints

- **GraphQL Playground**: `/graphql`
- **API Documentation**: `/docs`
- **Health Check**: `/health`
- **Dashboard**: `/dashboard`

## 🧪 Testing

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=src

# Run specific test file
poetry run pytest tests/test_main.py
```

## 🐳 Docker Deployment

```bash
# Build image
docker build -t ui-ai-agent-backend .

# Run container
docker run -p 8000:8000 ui-ai-agent-backend
```

## 🚀 Production Deployment

### Render Deployment

The application is configured for automatic deployment on Render with:

- **Automatic Migrations**: Database migrations run during build and startup
- **Health Checks**: Built-in monitoring and health verification
- **Environment Management**: Production-ready configuration

See [PRODUCTION_MIGRATIONS.md](./PRODUCTION_MIGRATIONS.md) for detailed information about production database migrations.

### Migration Scripts

```bash
# Production migrations
./scripts/production-migrate.sh

# Development migrations
./scripts/migrate-db.sh apply

# Check migration status
./scripts/migrate-db.sh status
```

## 🌐 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ENVIRONMENT` | Environment name | `development` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://...` |
| `FRONTEND_URL` | Frontend URL for CORS | `http://localhost:3000` |

## 📊 Monitoring

- Health check endpoint: `/health`
- CORS configuration: `/cors-config`
- Environment info in health response

## 🔐 Security

- CORS configured for frontend domains
- Environment-specific security headers
- Input validation with Pydantic models