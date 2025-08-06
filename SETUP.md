# 🚀 UI AI Agent - Setup Guide

Complete setup guide for the UI AI Agent with GraphQL API and PostgreSQL database.

## 🏗️ Architecture

- **Backend**: FastAPI with Strawberry GraphQL
- **Database**: PostgreSQL (local Docker / Render production)
- **ORM**: SQLModel (SQLAlchemy-based)
- **Deployment**: GitHub Actions → Render (backend) / Vercel (frontend)

## 🎯 Quick Start

### Local Development

1. **Clone and setup:**
   ```bash
   git clone <your-repo>
   cd UI-AI-AGENT
   ```

2. **Start everything (Full Stack):**
   ```bash
   ./scripts/start.sh
   ```

3. **Or start backend only:**
   ```bash
   cd backend
   ./scripts/start-backend.sh
   ```

4. **Access services:**
   - **Frontend**: http://localhost:3000
   - **Backend**: http://localhost:8000
   - **Dashboard**: http://localhost:8000/dashboard
   - **GraphQL**: http://localhost:8000/graphql
   - **API Docs**: http://localhost:8000/docs
   - **pgAdmin**: http://localhost:5050

### Production Deployment (Render)

1. **Connect your GitHub repo to Render**
2. **Use the `render.yaml` configuration**
3. **Set environment variables in Render dashboard**
4. **Deploy automatically**

## 📁 Project Structure

```
UI-AI-AGENT/
├── backend/
│   ├── src/
│   │   ├── api/graphql/          # GraphQL schema & router
│   │   ├── core/config/          # Database & production config
│   │   ├── models/entities/      # SQLModel entities
│   │   └── ...
│   ├── scripts/                  # Backend utility scripts
│   ├── requirements.txt          # Render compatibility
│   └── pyproject.toml           # Poetry dependencies
├── frontend/                     # React/Next.js frontend
│   └── scripts/                  # Frontend utility scripts
├── scripts/                      # Project-wide scripts
├── docker-compose.yml           # Local PostgreSQL setup
├── .github/                     # GitHub Actions CI/CD
└── README.md                    # Project documentation
```

## 🔧 Local Development Scripts

### Available Scripts

| Script | Location | Purpose | Usage |
|--------|----------|---------|-------|
| `start.sh` | `scripts/` | Full stack (DB + API + Frontend) | `./scripts/start.sh` |
| `stop.sh` | `scripts/` | Stop all services | `./scripts/stop.sh` |
| `start-backend.sh` | `backend/scripts/` | Backend only (DB + API) | `cd backend && ./scripts/start-backend.sh` |
| `start-database.sh` | `backend/scripts/` | Database only | `cd backend && ./scripts/start-database.sh` |
| `stop-database.sh` | `backend/scripts/` | Stop database | `cd backend && ./scripts/stop-database.sh` |
| `reset-database.sh` | `backend/scripts/` | Fresh database | `cd backend && ./scripts/reset-database.sh` |

### Manual Setup

```bash
# 1. Start database
cd backend
./scripts/start-database.sh

# 2. Install dependencies
poetry install

# 3. Set environment
export DATABASE_URL="postgresql://postgres:postgres@localhost:5434/ui_ai_agent"
export FRONTEND_URL="http://localhost:3000"
export ENVIRONMENT="development"

# 4. Start server
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🌐 Available Endpoints

| Endpoint | Description | Local URL | Production URL |
|----------|-------------|-----------|----------------|
| **Dashboard** | Custom GraphQL UI | `http://localhost:8000/dashboard` | `https://your-app.onrender.com/dashboard` |
| **GraphQL** | Interactive playground | `http://localhost:8000/graphql` | `https://your-app.onrender.com/graphql` |
| **API Docs** | FastAPI documentation | `http://localhost:8000/docs` | `https://your-app.onrender.com/docs` |
| **Health** | System status | `http://localhost:8000/health` | `https://your-app.onrender.com/health` |

## 🗄️ Database Configuration

### Local Development
- **Host**: `localhost`
- **Port**: `5434`
- **Database**: `ui_ai_agent`
- **Username**: `postgres`
- **Password**: `postgres`

### Production (Render)
- **Host**: Auto-configured by Render
- **Database**: `ui_ai_agent`
- **SSL**: Required (auto-configured)
- **Connection**: Via `DATABASE_URL` environment variable

## 🔧 Environment Variables

### Local Development
```bash
DATABASE_URL="postgresql://postgres:postgres@localhost:5434/ui_ai_agent"
FRONTEND_URL="http://localhost:3000"
ENVIRONMENT="development"
DEBUG="true"
```

### Production (Render)
```bash
DATABASE_URL="postgresql://user:pass@host:port/db?sslmode=require"
FRONTEND_URL="https://your-frontend-domain.com"
ENVIRONMENT="production"
DEBUG="false"
LOG_LEVEL="INFO"
```

## 🚀 Production Deployment

The application is automatically deployed to production through GitHub Actions when changes are merged to the `main` branch.

### Deployment Process
1. **Push to GitHub** - Your changes trigger the CI/CD pipeline
2. **Automatic Testing** - Backend and frontend tests run
3. **Production Deployment** - Automatic deployment to Render (backend) and Vercel (frontend)
4. **Database Setup** - PostgreSQL database is automatically configured

### Environment Variables
The following environment variables are automatically set in production:
- `DATABASE_URL` - PostgreSQL connection string
- `ENVIRONMENT=production`
- `FRONTEND_URL` - Your frontend domain
- `DEBUG=false`
- `LOG_LEVEL=INFO`

## 🧪 Testing

### Test GraphQL Queries
```bash
# Test hello query
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ hello }"}'

# Test users query
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ users { id email username } }"}'
```

### Test Health Check
```bash
curl http://localhost:8000/health
```

## 📊 Database Schema

### Users Table
- `id` (UUID, Primary Key)
- `email` (VARCHAR, Unique)
- `username` (VARCHAR, Unique)
- `full_name` (VARCHAR)
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

### Jobs Table
- `id` (UUID, Primary Key)
- `title` (VARCHAR)
- `description` (TEXT)
- `company` (VARCHAR)
- `location` (VARCHAR)
- `salary_min` (INTEGER)
- `salary_max` (INTEGER)
- `job_type` (VARCHAR)
- `status` (VARCHAR)
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

## 🔍 GraphQL Examples

### Queries
```graphql
# Get all users
query {
  users {
    id
    email
    username
    fullName
  }
}

# Get jobs by status
query {
  jobs(status: "active") {
    id
    title
    company
    location
  }
}
```

### Mutations
```graphql
# Create user
mutation {
  createUser(userData: {
    email: "new@example.com"
    username: "newuser"
    fullName: "New User"
  }) {
    id
    email
  }
}

# Create job
mutation {
  createJob(jobData: {
    title: "Developer"
    company: "TechCorp"
    location: "Remote"
    jobType: "full-time"
  }) {
    id
    title
  }
}
```

## 🚨 Troubleshooting

### Local Issues
```bash
# Check if containers are running
docker compose ps

# View logs
docker compose logs postgres

# Restart everything
cd backend
./reset-database.sh
./start-backend.sh
```

### Production Issues
1. **Check Render logs** in the dashboard
2. **Verify environment variables** are set correctly
3. **Test database connection** via health endpoint
4. **Check CORS settings** if frontend can't connect

### Common Problems
- **Port conflicts**: Change ports in docker-compose.yml
- **Database connection**: Verify DATABASE_URL format
- **CORS errors**: Update FRONTEND_URL in environment
- **Import errors**: Ensure all dependencies are installed

## 📞 Support

For issues:
1. Check the troubleshooting section above
2. Verify environment variables
3. Check logs in Render dashboard (production)
4. Ensure Docker is running (local development)

## 🎯 Next Steps

1. **Customize the GraphQL schema** for your needs
2. **Add authentication** to secure your API
3. **Build a frontend** to consume the GraphQL API
4. **Add more database models** as required
5. **Set up monitoring** and logging 