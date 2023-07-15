import sqlite3
from ..constants.global_constants import DB_NAME
from ..exceptions.IshopExceptions import NoDataFoundError, InsufficientStockError
from ..utils.connection import SingleConnection
# for key, value in row.items():
#     product[key.lower()] = value
# return product


def sell_product(customer_name, items: list, user_id):
    connection = SingleConnection()

    cur = connection.cursor()

    query = """
        INSERT INTO SALES (CUSTOMER_NAME, PRODUCT_ID, SOLD_UNITS, SOLD_BY)
        VALUES (?,?,?,?) RETURNING ID, CUSTOMER_NAME, PRODUCT_ID, SOLD_UNITS, SOLD_BY, SOLD_DATE
    """
    transactions = []
    for item in items:
        item = dict(item)
        product_id = item['product_id']
        sold_unit = item['sold_units']
        cur.execute(query, (customer_name, product_id, sold_unit, user_id))
        transactions.append(dict(cur.fetchone()))

    query = """
        UPDATE PRODUCT SET UNITS_IN_STOCK = UNITS_IN_STOCK - ? WHERE ID = ? 
    """

    try:
        for transaction in transactions:
            product_id = transaction['PRODUCT_ID']
            sold_units = transaction['SOLD_UNITS']
            cur.execute(query, (sold_units, product_id))
    except sqlite3.IntegrityError:
        raise InsufficientStockError()

    transaction_ids = ",".join([str(transaction['ID'])
                                for transaction in transactions])

    query = f"""
        SELECT S.id AS SALES_ID,
        S.PRODUCT_ID AS PRODUCT_ID, P.NAME AS PRODUCT_NAME,
        S.SOLD_UNITS AS SOLD_UNITS, P.SELL_PRICE AS COST_PER_ITEM,
        S.SOLD_UNITS*P.SELL_PRICE AS TOTAL_PRICE
        FROM PRODUCT P, SALES S
        WHERE P.ID = S.PRODUCT_ID 
        AND S.ID IN ({transaction_ids})
    """
    # print(transaction_ids)
    cur.execute(query)

    rows = cur.fetchall()

    if not rows:
        raise Exception("Some unknown error occurred")

    data = {}
    data['customer_name'] = customer_name
    data['items'] = []
    for row in rows:
        item = dict(row)
        bill_item = {'product_id': item['PRODUCT_ID'], 'product_name': item['PRODUCT_NAME'],
                     'units': item['SOLD_UNITS'], 'cost_per_unit': item['COST_PER_ITEM'],
                     'total_amount': item['TOTAL_PRICE']}
        data['items'].append(bill_item)
    data['total'] = sum([i['total_amount'] for i in data['items']])

    print(data)

    return data


def get_my_sales(user_id):
    connection = SingleConnection()
    cur = connection.cursor()
    # # id, CustomerName, ProductId, SoldUnits, SoldBy, SoldDate
    query = f"""
    SELECT ID, CUSTOMER_NAME, PRODUCT_ID, SOLD_UNITS, SOLD_BY, SOLD_DATE FROM 
    SALES WHERE SALES.SOLD_BY = ? ORDER BY ID ASC
    """
    cur.execute(query, (user_id,))
    rows = cur.fetchall()
    if not rows:
        raise NoDataFoundError("No Sales Data available")
    sales = []

    for row in rows:
        sale = dict()
        for key, value in dict(row).items():
            sale[key.lower()] = value
        sales.append(sale)

    return sales
