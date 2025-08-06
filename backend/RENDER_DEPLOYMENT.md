# Render Deployment Guide

## Current Issue
Your FastAPI application is failing to start because it can't connect to a PostgreSQL database. The error shows:
```
connection to server at "localhost" (::1), port 5434 failed: Connection refused
```

## Solution Steps

### Step 1: Create PostgreSQL Database in Render

1. Go to your Render dashboard: https://dashboard.render.com
2. Click "New" → "PostgreSQL"
3. Configure the database:
   - **Name**: `ui-ai-agent-db`
   - **Database**: `ui_ai_agent`
   - **User**: `ui_ai_agent_user`
   - **Plan**: Free
4. Click "Create Database"

### Step 2: Link Database to Your Web Service

1. Go to your web service (`ui-ai-agent-backend`)
2. Go to "Environment" tab
3. Add environment variable:
   - **Key**: `DATABASE_URL`
   - **Value**: Click "Link" and select your `ui-ai-agent-db` database
4. Save the changes

### Step 3: Redeploy Your Application

1. Go to your web service
2. Click "Manual Deploy" → "Deploy latest commit"
3. Wait for the deployment to complete

### Step 4: Verify Deployment

1. Check the deployment logs for any errors
2. Visit your application URL
3. Test the `/health` endpoint
4. Test the `/db-test` endpoint

## Alternative: Use Environment Variables

If you prefer to set the DATABASE_URL manually:

1. Get the connection string from your database service
2. Add it as an environment variable in your web service
3. The connection string should look like:
   ```
   postgresql://ui_ai_agent_user:password@host:port/ui_ai_agent?sslmode=require
   ```

## Troubleshooting

### If deployment still fails:

1. **Check environment variables**: Ensure `DATABASE_URL` is properly set
2. **Check database status**: Make sure the database service is running
3. **Check logs**: Look for specific error messages in the deployment logs
4. **Test connection**: Use the `/db-test` endpoint to verify database connectivity

### Common Issues:

1. **SSL Mode**: Render requires SSL connections. The code automatically adds `sslmode=require`
2. **Database not ready**: Sometimes the database takes a few minutes to be fully available
3. **Wrong connection string**: Make sure you're using the correct connection string from Render

## Manual Database Setup (if needed)

If you need to manually create tables:

1. Connect to your database using a PostgreSQL client
2. Run the SQL commands from `init.sql` (if available)
3. Or let the application create tables automatically on first run

## Environment Variables Reference

Required environment variables:
- `DATABASE_URL`: PostgreSQL connection string
- `ENVIRONMENT`: Set to "production"
- `FRONTEND_URL`: Your frontend URL
- `SECRET_KEY`: Secret key for the application

Optional environment variables:
- `DEBUG`: Set to "false" in production
- `LOG_LEVEL`: Set to "INFO" in production 