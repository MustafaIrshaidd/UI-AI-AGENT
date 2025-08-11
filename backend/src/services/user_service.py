from sqlmodel import Session, select
from typing import Optional, List
from uuid import UUID
from datetime import datetime

from src.models.entities.user import User
from src.models.requests.user_requests import CreateUserRequest, UpdateUserRequest
from src.models.responses.user_responses import UserResponse

class UserService:
    """Service class for user operations"""
    
    def __init__(self, db_session: Session):
        self.db = db_session
    
    def create_user(self, user_data: CreateUserRequest) -> User:
        """Create a new user"""
        # Check if user with email already exists
        existing_user = self.db.exec(
            select(User).where(User.email == user_data.email)
        ).first()
        
        if existing_user:
            raise ValueError(f"User with email {user_data.email} already exists")
        
        # Create new user
        user = User(
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            auth0_id=user_data.auth0_id,
            is_active=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        
        return user
    
    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        """Get user by ID"""
        return self.db.exec(select(User).where(User.id == user_id)).first()
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.db.exec(select(User).where(User.email == email)).first()
    
    def get_user_by_auth0_id(self, auth0_id: str) -> Optional[User]:
        """Get user by Auth0 ID"""
        return self.db.exec(select(User).where(User.auth0_id == auth0_id)).first()
    
    def get_all_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Get all users with pagination"""
        return self.db.exec(select(User).offset(skip).limit(limit)).all()
    
    def update_user(self, user_id: UUID, user_data: UpdateUserRequest) -> Optional[User]:
        """Update an existing user"""
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        # Update fields if provided
        if user_data.username is not None:
            user.username = user_data.username
        if user_data.full_name is not None:
            user.full_name = user_data.full_name
        if user_data.is_active is not None:
            user.is_active = user_data.is_active
        
        user.updated_at = datetime.utcnow()
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        
        return user
    
    def delete_user(self, user_id: UUID) -> bool:
        """Delete a user (soft delete by setting is_active to False)"""
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        user.is_active = False
        user.updated_at = datetime.utcnow()
        
        self.db.add(user)
        self.db.commit()
        
        return True 