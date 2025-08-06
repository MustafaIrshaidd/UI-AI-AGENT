from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool
from sqlalchemy.exc import OperationalError
import os
import time
from typing import Generator
from .production import ProductionConfig

# Get database URL from production config
DATABASE_URL = ProductionConfig.get_database_url()

print(f"Initializing database connection to: {DATABASE_URL[:50]}...")

# Create engine with production-optimized settings
engine = create_engine(
    DATABASE_URL,
    echo=ProductionConfig.DEBUG,  # Only echo in debug mode
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=300,  # Recycle connections every 5 minutes
    pool_timeout=30,  # Wait up to 30 seconds for a connection
    max_overflow=10,  # Allow up to 10 connections beyond pool size
    connect_args={
        "check_same_thread": False
    } if "sqlite" in DATABASE_URL else {}
)

def create_db_and_tables():
    """Create database tables with retry logic"""
    max_retries = 5
    retry_delay = 2
    
    for attempt in range(max_retries):
        try:
            print(f"Attempting to create database tables (attempt {attempt + 1}/{max_retries})")
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
                print("Max retries reached. Database connection failed.")
                print("This is likely because:")
                print("1. DATABASE_URL environment variable is not set")
                print("2. Database service is not running")
                print("3. Database credentials are incorrect")
                print("4. Network connectivity issues")
                print("Please check your Render deployment configuration.")
                # Don't raise the exception - let the app start without database
                print("Continuing without database initialization...")
                return

def get_session() -> Generator[Session, None, None]:
    """Dependency to get database session"""
    with Session(engine) as session:
        yield session 