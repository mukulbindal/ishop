from fastapi import HTTPException
from ..repository.user import login
from ..schema.schemas import LoginRequest, LoginResponse, User
from ..utils.auth_utils import generate_token
from ..utils.utils import error_handler
from ..utils.auth_utils import verify_password


@error_handler
def login_service(login_request: LoginRequest):
    user: User = login(login_request.username)

    if verify_password(login_request.password, user.password):
        return LoginResponse(username=user.username, token=generate_token(dict(user)))
    else:
        raise HTTPException(
            status_code=401, detail="Invalid Username or Password")
