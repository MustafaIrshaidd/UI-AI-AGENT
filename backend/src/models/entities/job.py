from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

class Job(SQLModel, table=True):
    __tablename__ = "jobs"
    
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(index=True)
    description: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_type: Optional[str] = None
    status: str = Field(default="active", index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class JobCreate(SQLModel):
    title: str
    description: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_type: Optional[str] = None
    status: Optional[str] = "active"

class JobUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_type: Optional[str] = None
    status: Optional[str] = None

class JobRead(SQLModel):
    id: UUID
    title: str
    description: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_type: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: datetime 