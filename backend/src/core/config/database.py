from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool
import os
from typing import Generator
from .production import ProductionConfig

# Get database URL from production config
DATABASE_URL = ProductionConfig.get_database_url()

# Create engine with production-optimized settings
engine = create_engine(
    DATABASE_URL,
    echo=ProductionConfig.DEBUG,  # Only echo in debug mode
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=300,  # Recycle connections every 5 minutes
    connect_args={
        "check_same_thread": False
    } if "sqlite" in DATABASE_URL else {}
)

def create_db_and_tables():
    """Create database tables"""
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Dependency to get database session"""
    with Session(engine) as session:
        yield session 