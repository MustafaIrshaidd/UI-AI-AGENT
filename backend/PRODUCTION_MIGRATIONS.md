# Production Database Migrations Guide

This guide explains how database migrations are handled in production on Render for the UI AI Agent Backend.

## Overview

The application automatically handles database migrations in three ways:

1. **Render Build Process**: Migrations run during the build phase
2. **Docker Container Startup**: Migrations run before the application starts
3. **Manual Migration Scripts**: For emergency situations

## Automatic Migration Process

### 1. Render Build Process

When deploying to Render, the `render.yaml` configuration includes:

```yaml
buildCommand: |
  pip install poetry
  poetry config virtualenvs.create false
  poetry install --no-dev
  # Run database migrations
  poetry run alembic upgrade head
```

This ensures that:
- Dependencies are installed
- Database migrations are applied
- The application starts with an up-to-date database schema

### 2. Docker Container Startup

The `Dockerfile` includes a startup script that:
- Checks current migration status
- Applies any pending migrations
- Starts the application only after migrations are complete

## Manual Migration Options

### Production Migration Script

For manual migrations or troubleshooting, use the production migration script:

```bash
cd backend
./scripts/production-migrate.sh
```

This script:
- ✅ Checks database connectivity with retries
- ✅ Verifies if migrations are needed
- ✅ Applies migrations safely
- ✅ Verifies migration success
- ✅ Provides detailed logging

### Standard Migration Script

For development and testing:

```bash
cd backend
./scripts/migrate-db.sh apply
```

## Migration Safety Features

### Connection Retry Logic
- Attempts database connection up to 5 times
- 10-second delays between attempts
- Graceful failure handling

### Migration Verification
- Checks current vs. target migration versions
- Verifies database connectivity after migrations
- Provides detailed status reporting

### Rollback Capability
```bash
# Rollback to specific revision
./scripts/migrate-db.sh rollback <revision_id>

# Show available revisions
./scripts/migrate-db.sh status
```

## Environment Variables

Ensure these are set in your Render environment:

- `DATABASE_URL`: Connection string to your PostgreSQL database
- `ENVIRONMENT`: Set to "production"
- `DEBUG`: Set to "false"

## Monitoring and Logs

### Migration Logs
Migrations are logged to Render's application logs. Monitor for:
- ✅ "Migrations completed successfully"
- ❌ "Migration failed" messages
- 🔍 Connection retry attempts

### Health Checks
The application includes health checks that verify:
- Application responsiveness
- Database connectivity
- Overall system health

## Troubleshooting

### Common Issues

1. **Connection Timeouts**
   - Check database URL configuration
   - Verify network connectivity
   - Check Render database status

2. **Migration Failures**
   - Review migration files for syntax errors
   - Check database permissions
   - Verify schema compatibility

3. **Build Failures**
   - Check Poetry dependency resolution
   - Verify Python version compatibility
   - Review build logs for specific errors

### Emergency Procedures

If automatic migrations fail:

1. **Stop the deployment** in Render
2. **Manually run migrations** using the production script
3. **Verify database state** before redeploying
4. **Check logs** for specific error messages

## Best Practices

### Before Deployment
- ✅ Test migrations locally
- ✅ Review migration files
- ✅ Backup production database
- ✅ Plan rollback strategy

### During Deployment
- ✅ Monitor build logs
- ✅ Verify migration success
- ✅ Check application health
- ✅ Monitor error rates

### After Deployment
- ✅ Verify application functionality
- ✅ Check database schema
- ✅ Monitor performance metrics
- ✅ Review error logs

## Migration History

Track your migration history:

```bash
# Show current status
poetry run alembic current

# Show migration history
poetry run alembic history --verbose

# Show specific migration details
poetry run alembic show <revision_id>
```

## Support

For migration-related issues:

1. Check Render application logs
2. Review migration script output
3. Verify database connectivity
4. Check Alembic configuration
5. Review recent code changes

---

**Note**: Always test migrations in a staging environment before applying to production. The automatic migration system provides safety, but manual verification is recommended for critical deployments. 