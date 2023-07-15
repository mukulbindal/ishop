from fastapi import HTTPException
from ..schema.schemas import IShopException
from ..exceptions.IshopExceptions import NoDataFoundError


def error_handler(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except NoDataFoundError as e:
            return IShopException(status=e.status, message=e.msg)
        except HTTPException as e:
            return IShopException(status=e.status_code, message=e.detail)
        except Exception as e:
            print(e, e.__class__)
            return IShopException(status=500, message=str(e))
    return wrapper
