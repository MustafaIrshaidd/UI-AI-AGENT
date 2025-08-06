import os
from typing import Optional

class ProductionConfig:
    """Production configuration for Render deployment"""
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # Database configuration - prioritize DATABASE_URL from environment
    _DATABASE_URL: str = os.getenv("DATABASE_URL")
    
    # Only use fallback if DATABASE_URL is not set
    if not _DATABASE_URL:
        _DATABASE_URL = "postgresql://postgres:postgres@localhost:5434/ui_ai_agent"
        print("WARNING: DATABASE_URL not set, using fallback localhost URL")
    else:
        print(f"Using DATABASE_URL from environment: {_DATABASE_URL[:50]}...")
    
    # Handle Render's DATABASE_URL format (add sslmode if needed)
    if _DATABASE_URL.startswith("postgres://"):
        _DATABASE_URL = _DATABASE_URL.replace("postgres://", "postgresql://", 1)
        print("Converted postgres:// to postgresql://")
    
    # Add SSL mode for production databases (especially Render)
    if ("render.com" in _DATABASE_URL or "localhost" not in _DATABASE_URL) and "sslmode" not in _DATABASE_URL:
        if "?" in _DATABASE_URL:
            _DATABASE_URL += "&sslmode=require"
        else:
            _DATABASE_URL += "?sslmode=require"
        print("Added SSL mode to database URL")
    
    DATABASE_URL: str = _DATABASE_URL
    
    # API configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    # CORS configuration
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    
    # Get environment-specific origins
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")
    
    # Development origins
    # Port 3000: Main frontend development server (React/Next.js default)
    DEV_ORIGINS: list = [
        "http://localhost:3000",  # Main frontend with and without trailing slash
        "http://localhost:3000/",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3000/"
    ]
    # Production origins - only use FRONTEND_URL
    PROD_ORIGINS: list = []
    
    # Add FRONTEND_URL from environment
    if FRONTEND_URL:
        PROD_ORIGINS = [FRONTEND_URL]
        # Also add version without trailing slash if FRONTEND_URL has one
        # Or add version with trailing slash if FRONTEND_URL doesn't have one
        if FRONTEND_URL.endswith('/'):
            PROD_ORIGINS.append(FRONTEND_URL.rstrip('/'))
        else:
            PROD_ORIGINS.append(f"{FRONTEND_URL}/")
    
    # Remove duplicates and filter out empty strings
    PROD_ORIGINS = list(set([origin for origin in PROD_ORIGINS if origin]))
    
    # Select origins based on environment
    ALLOWED_ORIGINS: list = PROD_ORIGINS if ENVIRONMENT.lower() == "production" else DEV_ORIGINS
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "ptp9hdwavYXXS-YJcSp0ptD2uNYSXg32ouD6qxP6iOM")
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def get_database_url(cls) -> str:
        """Get database URL with proper formatting for production"""
        return cls.DATABASE_URL
    
    @classmethod
    def is_production(cls) -> bool:
        """Check if running in production"""
        return cls.ENVIRONMENT.lower() == "production"
    
    @classmethod
    def get_cors_origins(cls) -> list:
        """Get allowed CORS origins"""
        origins = cls.ALLOWED_ORIGINS
        print(f"CORS Origins configured: {origins}")
        return origins 