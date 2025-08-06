from strawberry.fastapi import GraphQLRouter
from fastapi import Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlmodel import Session
import strawberry
from typing import Optional

from .schema import schema
from ...core.config.database import get_session

def get_context(session: Session = Depends(get_session)):
    return {"session": session}

# Enhanced GraphQL router with better configuration
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
    graphql_ide=True  # Enable GraphiQL playground
)

# Custom GraphQL dashboard HTML
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UI AI Agent - GraphQL Dashboard</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }
        .header p {
            margin: 10px 0 0 0;
            opacity: 0.9;
            font-size: 1.1em;
        }
        .content {
            padding: 30px;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        .stat-card h3 {
            margin: 0 0 10px 0;
            color: #333;
        }
        .stat-card p {
            margin: 0;
            font-size: 1.5em;
            font-weight: bold;
            color: #667eea;
        }
        .links {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }
        .link-card {
            background: #667eea;
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-decoration: none;
            text-align: center;
            transition: transform 0.2s;
        }
        .link-card:hover {
            transform: translateY(-2px);
        }
        .link-card h3 {
            margin: 0 0 10px 0;
        }
        .link-card p {
            margin: 0;
            opacity: 0.9;
        }
        .examples {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        .examples h3 {
            margin: 0 0 15px 0;
            color: #333;
        }
        .example-query {
            background: #2d3748;
            color: #e2e8f0;
            padding: 15px;
            border-radius: 6px;
            margin: 10px 0;
            font-family: 'Monaco', 'Menlo', monospace;
            font-size: 0.9em;
            overflow-x: auto;
        }
        .graphql-frame {
            border: none;
            width: 100%;
            height: 600px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 UI AI Agent</h1>
            <p>GraphQL API Dashboard</p>
        </div>
        
        <div class="content">
            <div class="stats">
                <div class="stat-card">
                    <h3>Database</h3>
                    <p>PostgreSQL</p>
                </div>
                <div class="stat-card">
                    <h3>API</h3>
                    <p>FastAPI + GraphQL</p>
                </div>
                <div class="stat-card">
                    <h3>ORM</h3>
                    <p>SQLModel</p>
                </div>
                <div class="stat-card">
                    <h3>Status</h3>
                    <p>🟢 Running</p>
                </div>
            </div>
            
            <div class="links">
                <a href="/graphql" class="link-card">
                    <h3>🔍 GraphQL Playground</h3>
                    <p>Interactive GraphQL IDE</p>
                </a>
                <a href="/docs" class="link-card">
                    <h3>📚 API Docs</h3>
                    <p>FastAPI Documentation</p>
                </a>
                <a href="http://localhost:5050" class="link-card" target="_blank">
                    <h3>🗄️ pgAdmin</h3>
                    <p>Database Management</p>
                </a>
                <a href="/health" class="link-card">
                    <h3>💚 Health Check</h3>
                    <p>System Status</p>
                </a>
            </div>
            
            <div class="examples">
                <h3>📝 Example GraphQL Queries</h3>
                
                <div class="example-query">
# Get all users
query {
  users {
    id
    email
    username
    fullName
    createdAt
  }
}
                </div>
                
                <div class="example-query">
# Get all jobs
query {
  jobs {
    id
    title
    company
    location
    salaryMin
    salaryMax
    jobType
    status
  }
}
                </div>
                
                <div class="example-query">
# Create a new user
mutation {
  createUser(userData: {
    email: "newuser@example.com"
    username: "newuser"
    fullName: "New User"
  }) {
    id
    email
    username
  }
}
                </div>
            </div>
            
            <iframe src="/graphql" class="graphql-frame"></iframe>
        </div>
    </div>
</body>
</html>
"""

# Dashboard endpoint
async def graphql_dashboard():
    """Custom GraphQL dashboard with enhanced UI"""
    return HTMLResponse(content=DASHBOARD_HTML) 