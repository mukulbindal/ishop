from fastapi import APIRouter, Depends, Request
from ..utils.auth_utils import JWTBearer
from ..service.product_service import create_product_service, edit_product_service, get_product_service, get_all_product_service, delete_product_service
from ..schema.schemas import ProductRequest, ProductEditRequest
product_router = APIRouter(prefix='/products')


@product_router.post('/add', tags=['Products'], dependencies=[Depends(JWTBearer())])
def create_product(product_req: ProductRequest, request: Request):
    return create_product_service(product_req, request.current_user)


@product_router.put('/edit', tags=['Products'], dependencies=[Depends(JWTBearer())])
def edit_product(product_req: ProductEditRequest, request: Request):
    return edit_product_service(product_req, request.current_user)


@product_router.get('/get', tags=['Products'], dependencies=[Depends(JWTBearer())])
def get_product(id):
    return get_product_service(id)


@product_router.get('/get-all', tags=['Products'], dependencies=[Depends(JWTBearer())])
def get_all_products():
    return get_all_product_service()


@product_router.delete('/remove', tags=['Products'], dependencies=[Depends(JWTBearer())])
def delete_products(id):
    return delete_product_service(id)
