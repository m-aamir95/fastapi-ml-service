from fastapi import APIRouter, Depends

from pydantic_models.data_models import UserBase
from database.database_connection import CustomizedDBSession

from services.user_service import UserService, SqlAlchemyUserService
#region Dependency Injection for the User Service
class GetUserService():

    def __init__(self):
        self.user_service : UserService = SqlAlchemyUserService(CustomizedDBSession)

    def __call__(self) -> UserService:
        
        return self.user_service

userService_dependency = GetUserService()
#endregion

router = APIRouter(
    prefix="/api/user",
    tags=["User"]
)

@router.post("/")
async def add_user(user : UserBase, user_service : UserService = Depends(userService_dependency)):
    
    return user_service.create_user(user.username, user.hashed_password)

