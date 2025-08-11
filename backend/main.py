from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

# Import database and configuration
from src.core.config.database import create_db_and_tables, engine
from src.core.config.production import ProductionConfig
from src.core.config.development import DevelopmentConfig

# Import routes
from src.routes import user_routes

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown"""
    # Startup
    create_db_and_tables()
    yield
    # Shutdown
    pass

app = FastAPI(
    title="UI AI Agent API",
    description="Basic FastAPI with database connection",
    version="1.0.0",
    lifespan=lifespan
)

# Use environment-specific configuration
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
if ENVIRONMENT.lower() == "production":
    config = ProductionConfig()
else:
    config = DevelopmentConfig()

# Get CORS origins
cors_origins = config.get_cors_origins()

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=86400,  # Cache preflight requests for 24 hours
)

# Include routers
app.include_router(user_routes.router)

# Basic endpoints for health and root
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with PostgreSQL!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "environment": ENVIRONMENT}

# Add server startup code
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )