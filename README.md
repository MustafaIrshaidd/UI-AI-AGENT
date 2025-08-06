# UI AI Agent

A full-stack web application with a FastAPI backend and Next.js frontend, featuring automated CI/CD pipeline with GitHub Actions.

## 🚀 Quick Start

### Prerequisites
- Node.js 20+
- Python 3.13+
- Poetry (for backend dependencies)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MustafaIrshaidd/UI-AI-AGENT.git
   cd UI-AI-AGENT
   ```

2. **Backend Setup**
   ```bash
   cd backend
   poetry install
   poetry run uvicorn main:app --reload
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## 🏗️ Project Structure

```
UI-AI-AGENT/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application
│   ├── tests/              # Backend tests
│   └── pyproject.toml      # Python dependencies
├── frontend/               # Next.js frontend
│   ├── app/                # Next.js app directory
│   ├── components/         # React components
│   └── package.json        # Node.js dependencies
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

- **[CI/CD Setup Guide](.github/README.md)** - Complete pipeline documentation
- **[Secrets Configuration](SECRETS_SETUP.md)** - Environment setup guide

## 🛠️ Technologies

### Backend
- **FastAPI** - Modern Python web framework
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
- **Render** - Backend hosting
- **Vercel** - Frontend hosting

## 🧪 Testing

### Backend Tests
```bash
cd backend
poetry run pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
npm run lint
npx tsc --noEmit
npm run build
```

## 📦 Deployment

The application is automatically deployed to production when changes are merged to the `main` branch.

- **Frontend**: https://ui-ai-agent-o535c0we7-mustafa-irshaids-projects.vercel.app
- **Backend**: Check your Render dashboard for the URL

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
