from pydantic import BaseModel, EmailStr
from typing import Optional

class CreateUserRequest(BaseModel):
    """Request model for creating a new user"""
    email: EmailStr
    username: Optional[str] = None
    family_name: Optional[str] = None
    last_name: Optional[str] = None
    auth0_id: Optional[str] = None

class UpdateUserRequest(BaseModel):
    """Request model for updating an existing user"""
    username: Optional[str] = None
    family_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None 