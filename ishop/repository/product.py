import sqlite3
from ..constants.global_constants import DB_NAME


def create_product(name, description, buy_price, sell_price, quantity, user_id):
    with sqlite3.connect(DB_NAME, check_same_thread=False) as connection:
        connection.row_factory = sqlite3.Row
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
    with sqlite3.connect(DB_NAME, check_same_thread=False) as connection:
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()
        query = f"""
        SELECT id, name, description, buy_price, sell_price, units_in_stock, LAST_UPDATED_BY, last_updated_date
        FROM PRODUCT WHERE ID = ?
        """
        cur.execute(query, (id,))
        row = dict(cur.fetchone())
        product = dict()
        for key, value in row.items():
            product[key.lower()] = value
        return product


def get_all_products():
    with sqlite3.connect(DB_NAME, check_same_thread=False) as connection:
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()
        query = f"""
        SELECT id, name, description, buy_price, sell_price, units_in_stock, LAST_UPDATED_BY, last_updated_date
        FROM PRODUCT
        """
        cur.execute(query)
        rows = cur.fetchall()
        products = []

        for row in rows:
            product = dict()
            for key, value in dict(row).items():
                product[key.lower()] = value
            products.append(product)
        return products


def edit_product(id, values, user_id):
    with sqlite3.connect(DB_NAME, check_same_thread=False) as connection:
        connection.row_factory = sqlite3.Row
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
        row = dict(cur.fetchone())
        connection.commit()
        product = dict()
        for key, value in row.items():
            product[key.lower()] = value
        return product


def delete_product(id):
    with sqlite3.connect(DB_NAME, check_same_thread=False) as connection:
        cur = connection.cursor()
        query = f"""
        DELETE FROM
        PRODUCT WHERE ID = ?
        """
        i = cur.execute(query, (id,))
        connection.commit()
        print(list(i))
        return i
