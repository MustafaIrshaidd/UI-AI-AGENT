import strawberry
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from ...core.config.database import get_session
from ...models.entities.user import User, UserCreate, UserUpdate, UserRead
from ...models.entities.job import Job, JobCreate, JobUpdate, JobRead

# User GraphQL Types
@strawberry.type
class UserType:
    id: UUID
    email: str
    username: str
    full_name: Optional[str]
    created_at: datetime
    updated_at: datetime

@strawberry.input
class UserCreateInput:
    email: str
    username: str
    full_name: Optional[str] = None

@strawberry.input
class UserUpdateInput:
    email: Optional[str] = None
    username: Optional[str] = None
    full_name: Optional[str] = None

# Job GraphQL Types
@strawberry.type
class JobType:
    id: UUID
    title: str
    description: Optional[str]
    company: Optional[str]
    location: Optional[str]
    salary_min: Optional[int]
    salary_max: Optional[int]
    job_type: Optional[str]
    status: str
    created_at: datetime
    updated_at: datetime

@strawberry.input
class JobCreateInput:
    title: str
    description: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_type: Optional[str] = None
    status: Optional[str] = "active"

@strawberry.input
class JobUpdateInput:
    title: Optional[str] = None
    description: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_type: Optional[str] = None
    status: Optional[str] = None

# Queries
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, GraphQL!"

    @strawberry.field
    def users(self, info) -> List[UserType]:
        session = info.context["session"]
        statement = select(User)
        users = session.exec(statement).all()
        return [UserType(**user.dict()) for user in users]

    @strawberry.field
    def user(self, info, id: UUID) -> Optional[UserType]:
        session = info.context["session"]
        statement = select(User).where(User.id == id)
        user = session.exec(statement).first()
        return UserType(**user.dict()) if user else None

    @strawberry.field
    def jobs(self, info, status: Optional[str] = None) -> List[JobType]:
        session = info.context["session"]
        statement = select(Job)
        if status:
            statement = statement.where(Job.status == status)
        jobs = session.exec(statement).all()
        return [JobType(**job.dict()) for job in jobs]

    @strawberry.field
    def job(self, info, id: UUID) -> Optional[JobType]:
        session = info.context["session"]
        statement = select(Job).where(Job.id == id)
        job = session.exec(statement).first()
        return JobType(**job.dict()) if job else None

# Mutations
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, user_data: UserCreateInput) -> UserType:
        session = info.context["session"]
        user = User(**user_data.__dict__)
        session.add(user)
        session.commit()
        session.refresh(user)
        return UserType(**user.dict())

    @strawberry.mutation
    def update_user(self, info, id: UUID, user_data: UserUpdateInput) -> Optional[UserType]:
        session = info.context["session"]
        statement = select(User).where(User.id == id)
        user = session.exec(statement).first()
        if not user:
            return None
        
        update_data = {k: v for k, v in user_data.__dict__.items() if v is not None}
        for key, value in update_data.items():
            setattr(user, key, value)
        
        user.updated_at = datetime.utcnow()
        session.add(user)
        session.commit()
        session.refresh(user)
        return UserType(**user.dict())

    @strawberry.mutation
    def delete_user(self, info, id: UUID) -> bool:
        session = info.context["session"]
        statement = select(User).where(User.id == id)
        user = session.exec(statement).first()
        if not user:
            return False
        
        session.delete(user)
        session.commit()
        return True

    @strawberry.mutation
    def create_job(self, info, job_data: JobCreateInput) -> JobType:
        session = info.context["session"]
        job = Job(**job_data.__dict__)
        session.add(job)
        session.commit()
        session.refresh(job)
        return JobType(**job.dict())

    @strawberry.mutation
    def update_job(self, info, id: UUID, job_data: JobUpdateInput) -> Optional[JobType]:
        session = info.context["session"]
        statement = select(Job).where(Job.id == id)
        job = session.exec(statement).first()
        if not job:
            return None
        
        update_data = {k: v for k, v in job_data.__dict__.items() if v is not None}
        for key, value in update_data.items():
            setattr(job, key, value)
        
        job.updated_at = datetime.utcnow()
        session.add(job)
        session.commit()
        session.refresh(job)
        return JobType(**job.dict())

    @strawberry.mutation
    def delete_job(self, info, id: UUID) -> bool:
        session = info.context["session"]
        statement = select(Job).where(Job.id == id)
        job = session.exec(statement).first()
        if not job:
            return False
        
        session.delete(job)
        session.commit()
        return True

# Create schema
schema = strawberry.Schema(query=Query, mutation=Mutation) 