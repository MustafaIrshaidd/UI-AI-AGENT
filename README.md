# 🚀 UI AI Agent

A modern web application with GraphQL API, PostgreSQL database, and beautiful dashboard interface. Features automated CI/CD pipeline with GitHub Actions.

## 🚀 Quick Start

### Prerequisites
- Node.js 20+
- Python 3.13+
- Poetry (for backend dependencies)
- Docker (for local database)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MustafaIrshaidd/UI-AI-AGENT.git
   cd UI-AI-AGENT
   ```

2. **Start everything (Full Stack):**
   ```bash
   ./scripts/start.sh
   ```

3. **Or start services separately:**
   ```bash
   # Backend only
   cd backend
   ./scripts/start-backend.sh
   
   # Frontend only (in another terminal)
   cd frontend
   npm install
   npm run dev
   ```

4. **Access the application**
   - **Frontend**: http://localhost:3000
   - **Backend**: http://localhost:8000
   - **Dashboard**: http://localhost:8000/dashboard
   - **GraphQL Playground**: http://localhost:8000/graphql
   - **API Docs**: http://localhost:8000/docs
   - **pgAdmin**: http://localhost:5050

## 🏗️ Project Structure

```
UI-AI-AGENT/
├── backend/                 # FastAPI GraphQL API
│   ├── src/
│   │   ├── api/graphql/    # GraphQL schema & router
│   │   ├── core/config/    # Database & production config
│   │   ├── models/         # SQLModel entities
│   │   └── ...
│   ├── scripts/            # Backend utility scripts
│   ├── requirements.txt    # Render compatibility
│   └── pyproject.toml      # Python dependencies
├── frontend/               # Next.js frontend
│   ├── app/                # Next.js app directory
│   ├── components/         # React components
│   ├── scripts/            # Frontend utility scripts
│   └── package.json        # Node.js dependencies
├── scripts/                # Project-wide scripts
├── docker-compose.yml      # Local database setup
├── render.yaml            # Production deployment
└── .github/                # CI/CD configuration
    ├── workflows/          # GitHub Actions workflows
    └── README.md           # CI/CD documentation
```

## 🔧 CI/CD Pipeline

This project features a comprehensive CI/CD pipeline with:

- **Automated Testing**: Backend and frontend tests on every commit
- **Code Quality**: Linting and type checking
- **Production Deployment**: Automated deployment to Render (backend) and Vercel (frontend)
- **Branch Protection**: Code review requirements and status checks
- **Automatic Cleanup**: Merged branches are automatically deleted

## 🔧 CORS Configuration

The application includes robust CORS configuration for production deployment:

- **Environment-aware**: Automatically switches between development and production settings
- **Flexible origins**: Supports multiple frontend domains via environment variables
- **Debug endpoints**: Built-in CORS configuration inspection
- **Comprehensive testing**: CORS test scripts for deployment verification

### Environment Variables for CORS

```bash
# Required for production
ENVIRONMENT=production
FRONTEND_URL=https://your-frontend-domain.com

# Optional: Additional domains
ADDITIONAL_CORS_ORIGINS=https://staging.domain.com,https://admin.domain.com
```

### Testing CORS

```bash
# Test CORS configuration
python backend/test_cors_deployment.py https://your-backend.onrender.com https://your-frontend.vercel.app

# Check CORS config endpoint
curl https://your-backend.onrender.com/cors-config
```

For detailed CORS troubleshooting, see [CORS_TROUBLESHOOTING.md](./backend/CORS_TROUBLESHOOTING.md).

### 📋 Workflow

1. **Feature Branch** → **Tests** → **PR to Dev**
2. **Dev Branch** → **Tests & Linting** → **PR to Main**
3. **Main Branch** → **Production Deployment** (with approval)

### 📚 Documentation

- **[SETUP.md](./SETUP.md)** - Complete setup and deployment guide
- **[CI/CD Setup Guide](.github/README.md)** - Complete pipeline documentation
- **[Secrets Configuration](SECRETS_SETUP.md)** - Environment setup guide
- **[API Documentation](http://localhost:8000/docs)** - Interactive API docs
- **[GraphQL Schema](http://localhost:8000/graphql)** - Schema exploration

## 📁 Scripts Organization

The project uses a well-organized script structure for easy management:

### Project-wide Scripts (`/scripts/`)
- `start.sh` - Start the entire application stack
- `stop.sh` - Stop all services and clean up

### Backend Scripts (`/backend/scripts/`)
- Database management (start, stop, reset)
- Development server management
- Build and deployment scripts

### Frontend Scripts (`/frontend/scripts/`)
- Environment setup and switching
- Configuration management

For detailed script documentation, see:
- [Project Scripts](./scripts/README.md)
- [Backend Scripts](./backend/scripts/README.md)
- [Frontend Scripts](./frontend/scripts/README.md)

## 🛠️ Technologies

### Backend
- **FastAPI** - Modern Python web framework
- **Strawberry GraphQL** - Type-safe GraphQL implementation
- **SQLModel** - SQLAlchemy-based ORM with Pydantic
- **PostgreSQL** - Production-ready database
- **Poetry** - Dependency management
- **Pytest** - Testing framework
- **Flake8** - Code linting

### Frontend
- **Next.js 15** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **ESLint** - Code linting

### DevOps
- **GitHub Actions** - CI/CD automation
- **Render** - Backend hosting with PostgreSQL
- **Vercel** - Frontend hosting
- **Docker** - Local development containers

## 🧪 Testing

### Backend Tests
```bash
cd backend
poetry run pytest tests/ -v
```

### GraphQL Testing
```bash
# Test GraphQL endpoint
curl -X POST http://localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ hello }"}'

# Test health endpoint
curl http://localhost:8000/health
```

### Frontend Tests
```bash
cd frontend
npm run lint
npx tsc --noEmit
npm run build
```

## 📦 Deployment

The application is automatically deployed to production through GitHub Actions when changes are merged to the `main` branch.

- **Frontend**: https://ui-ai-agent-o535c0we7-mustafa-irshaids-projects.vercel.app
- **Backend**: Automatically deployed to Render
- **GraphQL Playground**: Available at `/graphql` endpoint
- **Dashboard**: Available at `/dashboard` endpoint

### Production Features
- **PostgreSQL Database** - Managed by Render
- **SSL Encryption** - Automatic HTTPS
- **Environment Variables** - Secure configuration
- **Auto-scaling** - Based on traffic
- **CI/CD Pipeline** - Automated testing and deployment

## 🤝 Contributing

1. Create a feature branch from `dev`
2. Make your changes
3. Run tests locally
4. Create a pull request to `dev`
5. After review, merge to `dev`
6. Create a pull request from `dev` to `main` for production deployment

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For CI/CD pipeline issues, see the [CI/CD documentation](.github/README.md).
For deployment setup, see the [Secrets Setup Guide](SECRETS_SETUP.md).
