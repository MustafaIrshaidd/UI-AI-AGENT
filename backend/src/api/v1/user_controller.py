from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from src.core.config.database import get_session
from src.services.user_service import UserService
from src.models.requests.user_requests import (
    UpdateUserRequest,
    UpsertAuth0UserRequest,
)
from src.models.responses.user_responses import UserResponse, UserListResponse
from src.core.exceptions.user_exceptions import UserNotFoundException
from fastapi.responses import RedirectResponse
from src.api.middleware import get_auth0_claims, require_roles

router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(db: Session = Depends(get_session)) -> UserService:
    """Dependency injection for UserService"""
    return UserService(db)

@router.get("/", response_model=UserListResponse)
async def list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    user_service: UserService = Depends(get_user_service),
):
    """Get paginated list of users"""
    try:
        return user_service.get_users(skip=skip, limit=limit)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/smart/{identifier}", response_model=UserResponse)
async def get_user_smart(
    identifier: str,
    user_service: UserService = Depends(get_user_service),
):
    """Get user by either UUID or Auth0 ID, automatically detecting the type.
    
    This endpoint prevents UUID vs Auth0 ID casting errors by routing to the
    appropriate method based on the identifier format.
    """
    try:
        return user_service.get_user_by_id_or_auth0(identifier)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/all", response_model=list[UserResponse])
async def list_all_users(
    user_service: UserService = Depends(get_user_service),
):
    """Get all users without pagination (admin recommended)."""
    try:
        return user_service.get_all_users()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

# Admin-only: upsert arbitrary Auth0 payloads
@router.post("/auth0", response_model=UserResponse, status_code=200)
async def upsert_user_from_auth0(
    user_data: UpsertAuth0UserRequest,
    _claims: dict = Depends(require_roles(["admin"])),
    user_service: UserService = Depends(get_user_service),
):
    """Create or update a user based on Auth0 profile payload."""
    try:
        user = user_service.upsert_user_from_auth0(user_data)
        return user
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/me", response_model=UserResponse)
async def get_me(
    claims: dict = Depends(get_auth0_claims),
    user_service: UserService = Depends(get_user_service),
):
    """Resolve user from Auth0 token claims, upsert, and return profile."""

    print("🔍 I am in ME endpoint")
    print(f"📋 Claims received: {claims}")
    
    try:
        sub = str(claims.get("sub", ""))
        email = str(claims.get("email", ""))
        name = str(claims.get("name") or claims.get("nickname") or claims.get("email") or "")
        
        print(f"🔑 Extracted values:")
        print(f"   sub: {sub}")
        print(f"   email: {email}")
        print(f"   name: {name}")
        
        if not sub or not email or not name:
            print("❌ Missing required claims")
            raise HTTPException(status_code=400, detail="Invalid token: missing required claims")

        payload = UpsertAuth0UserRequest(
            auth0_id=sub,
            email=email,
            email_verified=bool(claims.get("email_verified", False)),
            given_name=claims.get("given_name") or claims.get("name", "").split()[0] if claims.get("name") else None,
            first_name=claims.get("first_name") or " ".join(claims.get("name", "").split()[1:]) if claims.get("name") and len(claims.get("name", "").split()) > 1 else None,
            nickname=claims.get("nickname"),
            picture=claims.get("picture"),
            last_login=None,
        )
        
        print(f"📦 Created payload: {payload}")
        print("🚀 Calling upsert_user_from_auth0...")
        
        result = user_service.upsert_user_from_auth0(payload)
        print(f"✅ Upsert successful: {result}")
        return result
        
    except Exception as e:
        print(f"❌ Error in /me endpoint: {str(e)}")
        print(f"❌ Error type: {type(e)}")
        import traceback
        print(f"❌ Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: str,
    user_service: UserService = Depends(get_user_service)
):
    """Get user by ID"""
    try:
        user = user_service.get_user_by_id(user_id)
        return user
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/by-auth0/{auth0_id}", response_model=UserResponse)
async def get_user_by_auth0_id(
    auth0_id: str,
    user_service: UserService = Depends(get_user_service),
):
    """Get a user by Auth0 ID"""
    try:
        return user_service.get_user_by_auth0_id(auth0_id)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

# Admin-only: update any user by id
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: str,
    user_data: UpdateUserRequest,
    _claims: dict = Depends(require_roles(["admin"])),
    user_service: UserService = Depends(get_user_service)
):
    """Update user"""
    try:
        user = user_service.update_user(user_id, user_data)
        return user
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
