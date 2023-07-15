from fastapi import APIRouter, Depends, Request
from ..utils.auth_utils import JWTBearer
from ..service.sales_service import sell_product_service, get_my_sales_service
from ..schema.schemas import SellProductRequest
sales_router = APIRouter(prefix='/sales')


@sales_router.post('/sell-product', tags=['Sales'], dependencies=[Depends(JWTBearer())], status_code=201)
def sell_product(product_req: SellProductRequest, request: Request):
    return sell_product_service(product_req, request.current_user)


@sales_router.get('/my-sales', tags=['Sales'], dependencies=[Depends(JWTBearer())], status_code=200)
def get_my_sales(request: Request):
    return get_my_sales_service(request.current_user)
