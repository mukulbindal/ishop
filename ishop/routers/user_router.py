from fastapi import APIRouter
from ..schema.schemas import LoginRequest
from ..service.user_service import login_service
user_router = APIRouter(prefix='/users')


@user_router.post('/login', tags=['Users'])
def login(login_request: LoginRequest):
    return login_service(login_request)
