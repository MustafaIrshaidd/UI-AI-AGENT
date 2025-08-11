import os
from typing import Optional

class DevelopmentConfig:
    """Development configuration for local development"""
    
    # Database configuration - will be validated when accessed
    _DATABASE_URL: Optional[str] = None
    
    @classmethod
    def get_database_url(cls) -> str:
        """Get database URL for development"""
        if cls._DATABASE_URL is None:
            cls._DATABASE_URL = os.getenv("DATABASE_URL")
            
            if not cls._DATABASE_URL:
                raise ValueError("DATABASE_URL environment variable must be set")
        
        return cls._DATABASE_URL
    
    # API configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    # CORS configuration for development
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:3000/",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3000/",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
        "http://localhost:3002",
        "http://127.0.0.1:3002",
        FRONTEND_URL,
    ]
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    
    # Security - will be validated when accessed
    _SECRET_KEY: Optional[str] = None
    
    @classmethod
    def get_secret_key(cls) -> str:
        """Get SECRET_KEY with validation"""
        if cls._SECRET_KEY is None:
            cls._SECRET_KEY = os.getenv("SECRET_KEY")
            
            if not cls._SECRET_KEY:
                raise ValueError("SECRET_KEY environment variable must be set")
        
        return cls._SECRET_KEY
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")
    

    
    @classmethod
    def is_production(cls) -> bool:
        """Check if running in production"""
        return cls.ENVIRONMENT.lower() == "production"
    
    @classmethod
    def get_cors_origins(cls) -> list:
        """Get allowed CORS origins for development"""
        return cls.ALLOWED_ORIGINS 