from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from uuid import uuid4, UUID

class User(SQLModel, table=True):
    """User entity model"""
    
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    username: Optional[str] = Field(default=None, unique=True, index=True)
    family_name: Optional[str] = Field(default=None, index=True)
    last_name: Optional[str] = Field(default=None, index=True)
    auth0_id: Optional[str] = Field(default=None, unique=True, index=True)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        table_name = "users" 