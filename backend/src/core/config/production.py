import os
from typing import Optional

class ProductionConfig:
    """Production configuration for Render deployment"""
    
    # Database configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5434/ui_ai_agent")
    
    # Handle Render's DATABASE_URL format (add sslmode if needed)
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    # Add SSL mode for production databases
    if "render.com" in DATABASE_URL and "sslmode" not in DATABASE_URL:
        if "?" in DATABASE_URL:
            DATABASE_URL += "&sslmode=require"
        else:
            DATABASE_URL += "?sslmode=require"
    
    # API configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    # CORS configuration
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    
    # Get environment-specific origins
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")
    
    # Development origins
    DEV_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:3000/",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3000/",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
        "http://localhost:3002",
        "http://127.0.0.1:3002"
    ]
    
    # Production origins - add your actual frontend domains here
    PROD_ORIGINS: list = [
        FRONTEND_URL,  # From environment variable
    ]
    
    # Select origins based on environment
    ALLOWED_ORIGINS: list = PROD_ORIGINS if ENVIRONMENT.lower() == "production" else DEV_ORIGINS
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    
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
        return cls.ALLOWED_ORIGINS 