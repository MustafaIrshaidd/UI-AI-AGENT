from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from uuid import UUID

from src.core.config.database import get_session
from src.services.user_service import UserService
from src.models.requests.user_requests import CreateUserRequest, UpdateUserRequest
from src.models.responses.user_responses import (
    UserResponse, 
    CreateUserResponse, 
    GetUserResponse, 
    ListUsersResponse
)

router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: Session = Depends(get_session)) -> UserService:
    """Dependency to get user service"""
    return UserService(db)

@router.post("/", response_model=CreateUserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: CreateUserRequest,
    user_service: UserService = Depends(get_user_service)
):
    """Create a new user"""
    try:
        user = user_service.create_user(user_data)
        user_response = UserResponse.model_validate(user, from_attributes=True)
        return CreateUserResponse(
            message="User created successfully",
            user=user_response
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create user"
        )

@router.get("/{user_id}", response_model=GetUserResponse)
def get_user(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service)
):
    """Get a user by ID"""
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user_response = UserResponse.model_validate(user, from_attributes=True)
    return GetUserResponse(user=user_response)

@router.get("/", response_model=ListUsersResponse)
def get_users(
    skip: int = 0,
    limit: int = 100,
    user_service: UserService = Depends(get_user_service)
):
    """Get all users with pagination"""
    users = user_service.get_all_users(skip=skip, limit=limit)
    user_responses = [
        UserResponse.model_validate(user, from_attributes=True) 
        for user in users
    ]
    
    return ListUsersResponse(users=user_responses, total=len(user_responses))

@router.get("/email/{email}", response_model=GetUserResponse)
def get_user_by_email(
    email: str,
    user_service: UserService = Depends(get_user_service)
):
    """Get a user by email"""
    user = user_service.get_user_by_email(email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user_response = UserResponse.model_validate(user, from_attributes=True)
    return GetUserResponse(user=user_response) 