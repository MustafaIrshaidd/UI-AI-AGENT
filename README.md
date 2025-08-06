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
   ./start.sh
   ```

3. **Or start services separately:**
   ```bash
   # Backend only
   cd backend
   ./start-backend.sh
   
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
│   ├── start-backend.sh    # Development script
│   ├── requirements.txt    # Render compatibility
│   └── pyproject.toml      # Python dependencies
├── frontend/               # Next.js frontend
│   ├── app/                # Next.js app directory
│   ├── components/         # React components
│   └── package.json        # Node.js dependencies
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
