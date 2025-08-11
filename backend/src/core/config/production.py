import os
from typing import Optional

class ProductionConfig:
    """Production configuration for Render deployment"""
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # Database configuration - will be validated when accessed
    _DATABASE_URL: Optional[str] = None
    
    @classmethod
    def get_database_url(cls) -> str:
        """Get database URL with proper formatting for production"""
        if cls._DATABASE_URL is None:
            cls._DATABASE_URL = os.getenv("DATABASE_URL")
            
            if not cls._DATABASE_URL:
                raise ValueError("DATABASE_URL environment variable must be set in production")
            
            print(f"Using DATABASE_URL from environment: {cls._DATABASE_URL[:50]}...")
            
            # Handle Render's DATABASE_URL format (add sslmode if needed)
            if cls._DATABASE_URL.startswith("postgres://"):
                cls._DATABASE_URL = cls._DATABASE_URL.replace("postgres://", "postgresql://", 1)
                print("Converted postgres:// to postgresql://")
            
            # Add SSL mode for production databases (especially Render)
            if ("render.com" in cls._DATABASE_URL or "localhost" not in cls._DATABASE_URL) and "sslmode" not in cls._DATABASE_URL:
                if "?" in cls._DATABASE_URL:
                    cls._DATABASE_URL += "&sslmode=require"
                else:
                    cls._DATABASE_URL += "?sslmode=require"
                print("Added SSL mode to database URL")
        
        return cls._DATABASE_URL
    
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
    
    # Security - will be validated when accessed
    _SECRET_KEY: Optional[str] = None
    
    @classmethod
    def get_secret_key(cls) -> str:
        """Get SECRET_KEY with validation"""
        if cls._SECRET_KEY is None:
            cls._SECRET_KEY = os.getenv("SECRET_KEY")
            
            if not cls._SECRET_KEY:
                raise ValueError("SECRET_KEY environment variable must be set in production")
        
        return cls._SECRET_KEY
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    

    
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