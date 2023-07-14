from fastapi import HTTPException
from ..schema.schemas import IShopException


def error_handler(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except HTTPException as e:
            return IShopException(status=e.status, message=str(e))
        except Exception as e:
            return IShopException(status=500, message=str(e))
    return wrapper
