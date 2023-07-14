import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..schema.schemas import User
SECRET_KEY = "THIS IS MY SECRET KEY"


def generate_token(data):
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')


def verify_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms='HS256')


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials, request):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str, request: Request) -> bool:
        isTokenValid: bool = False

        try:
            payload = verify_token(jwtoken)
            print(payload)
            user = User(
                id=payload['id'], username=payload['username'],
                password=payload['password'], designation=payload['designation'])
            print(user)
            request.current_user = user
        except Exception as e:
            print(e)
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
