# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy Poetry configuration files
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --only=main --no-root

# Copy application code
COPY . .

# Create startup script
RUN echo '#!/bin/bash\n\
echo "🚀 Starting UI AI Agent Backend..."\n\
echo "🔍 Checking if migrations are needed..."\n\
if poetry run alembic current &>/dev/null; then\n\
    echo "📊 Current migration status:"\n\
    poetry run alembic current\n\
    echo "🚀 Applying any pending migrations..."\n\
    poetry run alembic upgrade head\n\
    if [ $? -eq 0 ]; then\n\
        echo "✅ Migrations completed successfully"\n\
    else\n\
        echo "❌ Migration failed, but continuing..."\n\
    fi\n\
else\n\
    echo "⚠️  Could not check migration status, continuing..."\n\
fi\n\
echo "🚀 Starting application..."\n\
exec poetry run uvicorn main:app --host 0.0.0.0 --port 8000\n\
' > /app/start.sh && chmod +x /app/start.sh

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start the application with migrations
CMD ["/app/start.sh"] 