from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
import os
import time
from typing import Generator

# Import models to ensure they're registered with SQLModel metadata
from src.models.entities.user import User

def get_database_url():
    """Get database URL based on environment"""
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    if ENVIRONMENT.lower() == "production":
        from .production import ProductionConfig
        return ProductionConfig.get_database_url()
    else:
        from .development import DevelopmentConfig
        return DevelopmentConfig.get_database_url()

# Get database URL based on environment
DATABASE_URL = get_database_url()

print(f"Initializing database connection to: {DATABASE_URL[:50]}...")

def get_config():
    """Get configuration based on environment"""
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    if ENVIRONMENT.lower() == "production":
        from .production import ProductionConfig
        return ProductionConfig
    else:
        from .development import DevelopmentConfig
        return DevelopmentConfig

# Create engine with environment-appropriate settings
config = get_config()

engine = create_engine(
    DATABASE_URL,
    echo=config.DEBUG,  # Only echo in debug mode
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=300,  # Recycle connections every 5 minutes
    pool_timeout=30,  # Wait up to 30 seconds for a connection
    max_overflow=10,  # Allow up to 10 connections beyond pool size
    connect_args={
        "check_same_thread": False
    } if "sqlite" in DATABASE_URL else {}
)

def create_db_and_tables():
    """Create database tables if they don't exist"""
    max_retries = 5
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            print(f"Testing database connection (attempt {attempt + 1}/{max_retries})")
            # Test the connection
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Database connection successful")
            
            # Create all tables
            print("Creating database tables...")
            SQLModel.metadata.create_all(engine)
            print("Database tables created successfully")
            return
        except OperationalError as e:
            print(f"Database connection failed (attempt {attempt + 1}/{max_retries}): {str(e)}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                error_msg = "Max retries reached. Database connection failed. This is likely because: 1. DATABASE_URL environment variable is not set, 2. Database service is not running, 3. Database credentials are incorrect, or 4. Network connectivity issues. Please check your configuration."
                raise ConnectionError(error_msg)
                return

def get_session() -> Generator[Session, None, None]:
    """Dependency to get database session"""
    with Session(engine) as session:
        yield session 