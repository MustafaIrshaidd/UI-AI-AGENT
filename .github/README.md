# CI/CD Pipeline Documentation

## Overview
This repository uses GitHub Actions for continuous integration and deployment with the following workflow:

- **Development**: `dev` branch → Development environment
- **Production**: `main` branch → Production environment
- **Code Review**: All changes require pull request reviews

## Workflows

### 1. CI - Build and Test (`ci.yml`)
Runs on every push and pull request to `main` and `dev` branches.

**Backend CI:**
- Python 3.13 setup with Poetry
- Dependency installation and caching
- Linting with flake8
- Testing with pytest and coverage
- Coverage reporting to Codecov

**Frontend CI:**
- Node.js 20 setup with npm caching
- Dependency installation
- Linting with ESLint
- Type checking with TypeScript
- Build verification

### 2. Deploy to Development (`deploy-dev.yml`)
Triggers on pushes to `dev` branch.

**Features:**
- Automatic deployment to development environment
- Backend deployment to Render (dev)
- Frontend deployment to Vercel (dev)
- Sequential deployment (backend first, then frontend)

### 3. Deploy to Production (`deploy-prod.yml`)
Triggers on pushes to `main` branch.

**Features:**
- Manual approval required (environment protection)
- Security scanning (bandit, safety check)
- Backend deployment to Render (prod)
- Frontend deployment to Vercel (prod)
- Deployment success notifications

### 4. Branch Cleanup (`branch-cleanup.yml`)
Triggers when pull requests are merged.

**Features:**
- Automatic deletion of merged feature branches
- Protection of main and dev branches
- Cleanup of stale branches
- Safe deletion with error handling

### 5. Scheduled Cleanup (`scheduled-cleanup.yml`)
Runs weekly (Sundays at 2 AM UTC) or manually triggered.

**Features:**
- Generates branch cleanup reports
- Identifies merged branches for deletion
- Finds stale branches (older than 30 days)
- Provides detailed cleanup recommendations

## Branch Protection Rules

### Main Branch
- ✅ Requires 2 approving reviews
- ✅ Requires code owner review
- ✅ Requires status checks to pass
- ✅ Requires linear history
- ✅ Requires conversation resolution
- ❌ No force pushes allowed
- ❌ No deletions allowed

### Dev Branch
- ✅ Requires 1 approving review
- ✅ Requires status checks to pass
- ✅ Requires conversation resolution
- ❌ No force pushes allowed
- ❌ No deletions allowed

## Required Secrets

### Render (Backend)
```
RENDER_TOKEN_DEV=your_render_token_for_dev
RENDER_TOKEN_PROD=your_render_token_for_prod
RENDER_BACKEND_SERVICE_ID_DEV=your_dev_service_id
RENDER_BACKEND_SERVICE_ID_PROD=your_prod_service_id
```

### Vercel (Frontend)
```
VERCEL_TOKEN=your_vercel_token
VERCEL_ORG_ID=your_org_id
VERCEL_PROJECT_ID_DEV=your_dev_project_id
VERCEL_PROJECT_ID_PROD=your_prod_project_id
```

### Environment URLs
```
NEXT_PUBLIC_API_URL_DEV=https://your-dev-backend.onrender.com
NEXT_PUBLIC_API_URL_PROD=https://your-prod-backend.onrender.com
FRONTEND_PROD_URL=https://your-prod-frontend.vercel.app
BACKEND_PROD_URL=https://your-prod-backend.onrender.com
```

## Development Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write code
   - Add tests
   - Update documentation

3. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   # Create PR to dev branch
   ```

4. **Code Review**
   - At least 1 reviewer must approve for dev
   - At least 2 reviewers must approve for main
   - All CI checks must pass

5. **Merge to Dev**
   - Changes are automatically deployed to development
   - Feature branch is automatically deleted after merge

6. **Promote to Production**
   - Create PR from dev to main
   - Requires additional review
   - Manual approval for production deployment
   - Dev branch changes are preserved (not deleted)

## Environment Configuration

### Development Environment
- Backend: Render (development service)
- Frontend: Vercel (development project)
- Database: Development database
- Logging: Debug level

### Production Environment
- Backend: Render (production service)
- Frontend: Vercel (production project)
- Database: Production database
- Logging: Info level
- Security scanning enabled

## Monitoring and Alerts

- GitHub Actions provide real-time status updates
- Failed deployments trigger notifications
- Security scans run on production deployments
- Coverage reports are generated for each build

## Troubleshooting

### Common Issues

1. **CI Fails**
   - Check linting errors
   - Ensure all tests pass
   - Verify TypeScript compilation

2. **Deployment Fails**
   - Check environment secrets
   - Verify service IDs
   - Check Render/Vercel service status

3. **Review Requirements**
   - Ensure CODEOWNERS are set correctly
   - Check branch protection rules
   - Verify required status checks

### Getting Help
- Check GitHub Actions logs for detailed error messages
- Review environment configuration
- Contact repository administrators for access issues 