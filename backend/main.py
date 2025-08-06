from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

# Import database and GraphQL components
from src.core.config.database import create_db_and_tables, engine
from src.core.config.production import ProductionConfig
from src.core.config.development import DevelopmentConfig
from src.api.graphql.router import graphql_app
from src.api.graphql.dashboard import graphql_dashboard

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
    description="A FastAPI application with GraphQL and PostgreSQL",
    version="1.0.0",
    lifespan=lifespan
)

# Use environment-specific configuration
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
if ENVIRONMENT.lower() == "production":
    config = ProductionConfig()
else:
    config = DevelopmentConfig()
print(f"Environment: {config.ENVIRONMENT}")
print(f"Database URL: {config.get_database_url()[:50]}...")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.get_cors_origins(),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Include GraphQL router
app.include_router(graphql_app, prefix="/graphql")

# Add custom dashboard endpoint
@app.get("/dashboard")
async def dashboard():
    return await graphql_dashboard()

@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI with GraphQL and PostgreSQL!",
        "graphql_playground": "/graphql",
        "health_check": "/health"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "environment": config.ENVIRONMENT,
        "database_connected": "postgresql" in config.get_database_url(),
        "version": "1.0.0"
    }

@app.get("/db-test")
def test_database_connection():
    """Test database connection and return detailed status"""
    try:
        # Test the connection
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            result.fetchone()
        
        return {
            "status": "success",
            "message": "Database connection successful",
            "database_url": config.get_database_url()[:50] + "...",
            "environment": config.ENVIRONMENT
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Database connection failed: {str(e)}",
            "database_url": config.get_database_url()[:50] + "...",
            "environment": config.ENVIRONMENT,
            "error_type": type(e).__name__
        }

@app.get("/cors-config")
def cors_config():
    """Debug endpoint to show current CORS configuration"""
    return {
        "allowed_origins": config.get_cors_origins(),
        "environment": config.ENVIRONMENT,
        "frontend_url": config.FRONTEND_URL
    }
