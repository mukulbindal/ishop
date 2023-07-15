import sqlite3
from ..constants.global_constants import DB_NAME
from ..exceptions.IshopExceptions import NoDataFoundError
from ..utils.connection import SingleConnection


def create_product(name, description, buy_price, sell_price, quantity, user_id):
    connection = SingleConnection()
    cur = connection.cursor()
    query = f"""
    INSERT INTO PRODUCT (name, description, buy_price, sell_price, UNITS_IN_STOCK, LAST_UPDATED_BY)
    VALUES(?,?,?,?,?,?) returning id, name, description, buy_price, sell_price, units_in_stock, LAST_UPDATED_BY, last_updated_date
    """
    cur.execute(query, (name, description, buy_price,
                sell_price, quantity, user_id))
    row = dict(cur.fetchone())

    connection.commit()
    product = dict()
    for key, value in row.items():
        product[key.lower()] = value
    return product


def get_product(id):
    connection = SingleConnection()
    cur = connection.cursor()
    query = f"""
    SELECT id, name, description, buy_price, sell_price, units_in_stock, LAST_UPDATED_BY, last_updated_date
    FROM PRODUCT WHERE ID = ?
    """
    cur.execute(query, (id,))
    row = cur.fetchone()

    if not row:
        raise NoDataFoundError("Product does not exist")
    row = dict(row)
    product = dict()
    for key, value in row.items():
        product[key.lower()] = value

    return product


def get_all_products():
    connection = SingleConnection()
    cur = connection.cursor()
    query = f"""
    SELECT id, name, description, buy_price, sell_price, units_in_stock, LAST_UPDATED_BY, last_updated_date
    FROM PRODUCT
    """
    cur.execute(query)
    rows = cur.fetchall()
    if not rows:
        raise NoDataFoundError("No product available")
    products = []

    for row in rows:
        product = dict()
        for key, value in dict(row).items():
            product[key.lower()] = value
        products.append(product)

    return products


def edit_product(id, values, user_id):
    connection = SingleConnection()
    cur = connection.cursor()
    current_product = get_product(id)

    for key, value in values.items():
        current_product[key] = value

    new_values = (current_product['name'], current_product['description'], current_product['buy_price'],
                  current_product['sell_price'], current_product['units_in_stock'], user_id, id)
    query = f"""
    UPDATE PRODUCT set
    name = ?, description = ?, buy_price = ?, sell_price = ?, units_in_stock = ?, last_updated_by= ?,
    last_updated_date = datetime('now','localtime')
    where id=? returning id, name, description, buy_price, sell_price, units_in_stock, LAST_UPDATED_BY, last_updated_date
    """
    cur.execute(query, new_values)
    row = cur.fetchone()
    if not row:
        raise NoDataFoundError("The requested product was not found")
    row = dict(row)

    connection.commit()
    product = dict()
    for key, value in row.items():
        product[key.lower()] = value
    return product


def delete_product(id):
    connection = SingleConnection()
    cur = connection.cursor()
    query = f"""
    DELETE FROM
    PRODUCT WHERE ID = ?
    returning ID
    """
    cur.execute(query, (id,))
    i = cur.fetchone()
    if not i:
        raise NoDataFoundError("The requested product was not found")
    connection.commit()
    print(list(i))
    return {i[0]: "Deleted Successfully"}
