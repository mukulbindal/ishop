from ..repository.sales import sell_product, get_my_sales
from ..schema.schemas import SellProductRequest, Bill, User, Sales
from ..utils.utils import error_handler


@error_handler
def sell_product_service(pr: SellProductRequest, user: User):
    bill = sell_product(customer_name=pr.customer_name,
                        items=list(pr.items), user_id=user.id)
    return Bill.model_validate(bill)


@error_handler
def get_my_sales_service(user: User):
    sales = get_my_sales(user.id)
    return [Sales.model_validate(sale) for sale in sales]
