from ..repository.product import create_product, edit_product, get_all_products, get_product, delete_product
from ..schema.schemas import ProductRequest, User, Product, ProductEditRequest
from ..utils.utils import error_handler


@error_handler
def create_product_service(pr: ProductRequest, user: User):
    product = create_product(
        pr.name, pr.description, pr.buy_price, pr.sell_price, pr.units_in_stock, user.id)

    return Product.model_validate(product)


@error_handler
def edit_product_service(pr: ProductEditRequest, user: User):
    values = dict(pr)
    edited_product = edit_product(pr.id, values, user.id)
    return Product.model_validate(edited_product)


@error_handler
def get_product_service(id):
    product = get_product(id)
    return Product.model_validate(product)


@error_handler
def get_all_product_service():
    products = get_all_products()
    # Product.model_validate(product)
    return list(map(Product.model_validate, products))


@error_handler
def delete_product_service(id):
    return delete_product(id)
