from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    full_name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(SQLModel):
    email: str
    username: str
    full_name: Optional[str] = None

class UserUpdate(SQLModel):
    email: Optional[str] = None
    username: Optional[str] = None
    full_name: Optional[str] = None

class UserRead(SQLModel):
    id: UUID
    email: str
    username: str
    full_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime 