from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class UserResponse(BaseModel):
    """Response model for user data"""
    id: UUID
    email: str
    username: Optional[str] = None
    full_name: Optional[str] = None
    auth0_id: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

class CreateUserResponse(BaseModel):
    """Response model for user creation"""
    message: str
    user: UserResponse

class GetUserResponse(BaseModel):
    """Response model for getting a user"""
    user: UserResponse

class ListUsersResponse(BaseModel):
    """Response model for listing users"""
    users: list[UserResponse]
    total: int 