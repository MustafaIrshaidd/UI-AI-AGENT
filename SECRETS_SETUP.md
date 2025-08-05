# GitHub Secrets Setup Guide

This guide will help you configure all the required secrets for your CI/CD pipeline to work with Render (backend) and Vercel (frontend) for production deployment.

## 🔐 Required Secrets Overview

### For Production Environment (Required):
- `RENDER_TOKEN_PROD` - Render API token for production backend
- `RENDER_BACKEND_SERVICE_ID_PROD` - Render service ID for production backend
- `VERCEL_TOKEN` - Vercel API token
- `VERCEL_ORG_ID` - Vercel organization ID
- `VERCEL_PROJECT_ID_PROD` - Vercel project ID for production frontend
- `NEXT_PUBLIC_API_URL_PROD` - Production backend URL

### Optional (for notifications):
- `FRONTEND_PROD_URL` - Production frontend URL
- `BACKEND_PROD_URL` - Production backend URL

## 📝 Note: Development Environment

Since you're using free tiers of Render and Vercel, development deployments are not available. The `dev` branch will only run tests and linting, while production deployments happen when merging to `main`.

## 🚀 Step 1: Render Setup (Backend)

### 1.1 Get Render API Token
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click on your profile → **Account Settings**
3. Go to **API Keys** tab
4. Click **Create API Key**
5. Give it a name (e.g., "CI/CD Pipeline")
6. Copy the generated token

### 1.2 Create Production Backend Service
1. In Render Dashboard, click **New** → **Web Service**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `your-app-backend-prod`
   - **Environment**: `Python 3`
   - **Build Command**: `cd backend && pip install poetry && poetry install`
   - **Start Command**: `cd backend && poetry run uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Branch**: `main`
4. Click **Create Web Service**
5. Copy the **Service ID** from the service URL or settings

## 🎨 Step 2: Vercel Setup (Frontend)

### 2.1 Get Vercel API Token
1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **Settings** → **Tokens**
3. Click **Create Token**
4. Give it a name (e.g., "CI/CD Pipeline")
5. Set scope to **Full Account**
6. Copy the generated token

### 2.2 Get Organization ID
1. In Vercel Dashboard, go to **Settings** → **General**
2. Copy your **Team ID** (this is your organization ID)

### 2.3 Create Production Project
1. Click **New Project**
2. Import your GitHub repository
3. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Branch**: `main`
4. Click **Deploy**
5. Go to **Settings** → **General**
6. Copy the **Project ID**

## 🔧 Step 3: Add Secrets to GitHub

### 3.1 Go to GitHub Repository Settings
1. Go to your GitHub repository
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions**

### 3.2 Add Render Secrets
Click **New repository secret** and add:

```
Name: RENDER_TOKEN_PROD
Value: [Your Render API Token]

Name: RENDER_BACKEND_SERVICE_ID_PROD
Value: [Your Production Backend Service ID]
```

### 3.3 Add Vercel Secrets
```
Name: VERCEL_TOKEN
Value: [Your Vercel API Token]

Name: VERCEL_ORG_ID
Value: [Your Vercel Organization ID]

Name: VERCEL_PROJECT_ID_PROD
Value: [Your Production Frontend Project ID]
```

### 3.4 Add Environment URLs
```
Name: NEXT_PUBLIC_API_URL_PROD
Value: https://your-backend-prod.onrender.com

Name: FRONTEND_PROD_URL
Value: https://your-frontend-prod.vercel.app

Name: BACKEND_PROD_URL
Value: https://your-backend-prod.onrender.com
```

## ✅ Step 4: Test the Setup

### 4.1 Test Development Workflow
1. Push to `dev` branch
2. Check GitHub Actions tab
3. Verify tests and linting pass

### 4.2 Test Production Deployment
1. Create PR from `dev` to `main`
2. Merge the PR
3. Check GitHub Actions tab
4. Verify production deployment succeeds

## 🔍 Troubleshooting

### Common Issues:

1. **"Input required and not supplied: vercel-token"**
   - Make sure `VERCEL_TOKEN` secret is added
   - Check the secret name spelling

2. **"Render API error"**
   - Verify `RENDER_TOKEN_DEV` and `RENDER_TOKEN_PROD` are correct
   - Check if the service IDs are valid

3. **"Vercel deployment failed"**
   - Verify `VERCEL_ORG_ID` and project IDs are correct
   - Check if the Vercel token has proper permissions

4. **"Environment not found"**
   - Create the `development` and `production` environments in GitHub
   - Add required reviewers for production environment

### Getting Help:
- Check GitHub Actions logs for detailed error messages
- Verify all secrets are correctly named and have valid values
- Test API tokens manually before adding to secrets

## 🔄 Next Steps

After setting up secrets:
1. **Test the CI/CD pipeline** with a small change
2. **Configure branch protection rules** (see SETUP.md)
3. **Set up monitoring** for deployments
4. **Configure notifications** for deployment status

Your CI/CD pipeline will now be fully functional with automatic deployments to both development and production environments! 