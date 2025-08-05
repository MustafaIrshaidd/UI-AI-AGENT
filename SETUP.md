# CI/CD Pipeline Setup Guide

## Prerequisites

1. **GitHub Repository**: Ensure your repository is on GitHub
2. **Render Account**: For backend deployment
3. **Vercel Account**: For frontend deployment
4. **GitHub Personal Access Token**: For repository access

## Step 1: Repository Setup

### 1.1 Create Required Branches
```bash
# Create dev branch
git checkout -b dev
git push origin dev

# Return to main branch
git checkout main
```

### 1.2 Push CI/CD Configuration
```bash
# Add all new files
git add .

# Commit changes
git commit -m "feat: Add CI/CD pipeline with GitHub Actions

- Add CI workflow for testing and building
- Add development deployment workflow
- Add production deployment workflow
- Add branch protection rules
- Add CODEOWNERS file
- Add PR template
- Add comprehensive documentation"

# Push to main
git push origin main
```

## Step 2: GitHub Repository Settings

### 2.1 Enable Branch Protection

1. Go to your GitHub repository
2. Navigate to **Settings** → **Branches**
3. Click **Add rule** for the `main` branch
4. Configure the following settings:

**Main Branch Protection:**
- ✅ Require a pull request before merging
- ✅ Require approvals: **2**
- ✅ Dismiss stale pull request approvals when new commits are pushed
- ✅ Require review from code owners
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- ✅ Require linear history
- ✅ Require conversation resolution before merging
- ❌ Allow force pushes
- ❌ Allow deletions

**Dev Branch Protection:**
- ✅ Require a pull request before merging
- ✅ Require approvals: **1**
- ✅ Dismiss stale pull request approvals when new commits are pushed
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- ✅ Require conversation resolution before merging
- ❌ Allow force pushes
- ❌ Allow deletions

### 2.2 Create Environments

1. Go to **Settings** → **Environments**
2. Create **development** environment:
   - Name: `development`
   - Protection rules: None (for now)
3. Create **production** environment:
   - Name: `production`
   - Protection rules: ✅ Required reviewers (add yourself)

## Step 3: Render Setup (Backend)

### 3.1 Create Development Service
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **New** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `your-app-backend-dev`
   - **Environment**: `Python 3`
   - **Build Command**: `cd backend && pip install poetry && poetry install`
   - **Start Command**: `cd backend && poetry run uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Branch**: `dev`

### 3.2 Create Production Service
1. Create another web service
2. Configure:
   - **Name**: `your-app-backend-prod`
   - **Environment**: `Python 3`
   - **Build Command**: `cd backend && pip install poetry && poetry install`
   - **Start Command**: `cd backend && poetry run uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Branch**: `main`

### 3.3 Get Render Tokens and Service IDs
1. Go to **Account Settings** → **API Keys**
2. Create a new API key
3. Note down the service IDs from your services

## Step 4: Vercel Setup (Frontend)

### 4.1 Create Development Project
1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **New Project**
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Branch**: `dev`
   - **Environment Variables**:
     - `NEXT_PUBLIC_API_URL`: `https://your-backend-dev.onrender.com`
     - `NEXT_PUBLIC_ENVIRONMENT`: `development`

### 4.2 Create Production Project
1. Create another project or use the same with different branch
2. Configure:
   - **Branch**: `main`
   - **Environment Variables**:
     - `NEXT_PUBLIC_API_URL`: `https://your-backend-prod.onrender.com`
     - `NEXT_PUBLIC_ENVIRONMENT`: `production`

### 4.3 Get Vercel Tokens and IDs
1. Go to **Settings** → **Tokens**
2. Create a new token
3. Note down your Organization ID and Project IDs

## Step 5: GitHub Secrets Configuration

### 5.1 Add Repository Secrets
Go to **Settings** → **Secrets and variables** → **Actions**

Add the following secrets:

**Render Secrets:**
```
RENDER_TOKEN_DEV=your_render_api_key
RENDER_TOKEN_PROD=your_render_api_key
RENDER_BACKEND_SERVICE_ID_DEV=your_dev_service_id
RENDER_BACKEND_SERVICE_ID_PROD=your_prod_service_id
```

**Vercel Secrets:**
```
VERCEL_TOKEN=your_vercel_token
VERCEL_ORG_ID=your_org_id
VERCEL_PROJECT_ID_DEV=your_dev_project_id
VERCEL_PROJECT_ID_PROD=your_prod_project_id
```

**Environment URLs:**
```
NEXT_PUBLIC_API_URL_DEV=https://your-backend-dev.onrender.com
NEXT_PUBLIC_API_URL_PROD=https://your-backend-prod.onrender.com
FRONTEND_PROD_URL=https://your-frontend-prod.vercel.app
BACKEND_PROD_URL=https://your-backend-prod.onrender.com
```

## Step 6: Test the Pipeline

### 6.1 Test Development Deployment
```bash
# Create a feature branch
git checkout -b feature/test-pipeline

# Make a small change
echo "# Test" >> README.md

# Commit and push
git add README.md
git commit -m "test: Test CI/CD pipeline"
git push origin feature/test-pipeline

# Create PR to dev branch
# Wait for CI to pass and merge
# Verify deployment to development environment
```

### 6.2 Test Production Deployment
```bash
# Create PR from dev to main
# Wait for approval and merge
# Verify deployment to production environment
```

## Step 7: Monitoring and Maintenance

### 7.1 Set Up Notifications
1. Go to **Settings** → **Notifications**
2. Configure email notifications for:
   - Pull request reviews
   - Deployment status
   - Security alerts

### 7.2 Regular Maintenance
- Review and update dependencies monthly
- Monitor security alerts
- Check deployment logs regularly
- Update documentation as needed

## Troubleshooting

### Common Issues

1. **CI Fails on First Run**
   - Check if all dependencies are properly configured
   - Verify Python/Node.js versions match
   - Check for syntax errors in configuration files

2. **Deployment Fails**
   - Verify all secrets are correctly set
   - Check Render/Vercel service status
   - Review deployment logs for specific errors

3. **Branch Protection Issues**
   - Ensure CODEOWNERS file is in the correct location
   - Verify branch protection rules are properly configured
   - Check if required status checks are running

### Getting Help
- Check GitHub Actions logs for detailed error messages
- Review the `.github/README.md` for detailed documentation
- Contact repository administrators for access issues

## Next Steps

1. **Add More Tests**: Expand test coverage for both frontend and backend
2. **Security Scanning**: Integrate additional security tools
3. **Performance Monitoring**: Add performance monitoring and alerting
4. **Database Migrations**: Set up automated database migrations
5. **Backup Strategy**: Implement automated backups for production data 