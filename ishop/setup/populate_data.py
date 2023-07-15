import sqlite3
from ..utils.auth_utils import hash_password

CREATE_DM = False


def setup_db():
    global CREATE_DM
    DM_USER = '''
        CREATE TABLE IF NOT EXISTS USER(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME VARCHAR(20) UNIQUE NOT NULL,
        PASSWORD VARCHAR(255) NOT NULL,
        NAME VARCHAR(50) NOT NULL,
        DESIGNATION VARCHAR(30)
    )'''

    DM_PRODUCT = '''
        CREATE TABLE IF NOT EXISTS PRODUCT (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(100) NOT NULL,
        DESCRIPTION VARCHAR(200),
        BUY_PRICE NUMBER NOT NULL,
        UNITS_IN_STOCK NUMBER NOT NULL DEFAULT 0,
        SELL_PRICE NUMBER NOT NULL DEFAULT 0,
        LAST_UPDATED_BY INTEGER NOT NULL,
        LAST_UPDATED_DATE DATE DEFAULT (datetime('now','localtime')),
        FOREIGN KEY (LAST_UPDATED_BY) REFERENCES USER(ID),
        CHECK(BUY_PRICE>=0),
        CHECK(UNITS_IN_STOCK>=0),
        CHECK(SELL_PRICE>=0)
    )
    '''

    DM_SALES = '''
        CREATE TABLE IF NOT EXISTS SALES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CUSTOMER_NAME VARCHAR(255) NOT NULL,
        PRODUCT_ID INTEGER NOT NULL,
        SOLD_UNITS INTEGER NOT NULL,
        SOLD_BY INTEGER NOT NULL,
        SOLD_DATE DATE NOT NULL DEFAULT (datetime('now','localtime')),
        FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCT(ID),
        FOREIGN KEY (SOLD_BY) REFERENCES USER(ID),
        CHECK(SOLD_UNITS>0)
    )
    '''
    DM_CREATE_TABLE = [DM_USER, DM_PRODUCT, DM_SALES]

    print("Creating tables...")
    con = sqlite3.connect("ishop.db")

    cur = con.cursor()

    for query in DM_CREATE_TABLE:
        try:
            cur.execute(query)
        except Exception as e:
            print(e)

    con.commit()

    insert_data = [
        f"INSERT INTO USER(USERNAME, NAME, PASSWORD, DESIGNATION) VALUES ('mukul', 'Mukul', '{hash_password('Mukul@123')}', 'OWNER')",
        f"INSERT INTO USER(USERNAME, NAME, PASSWORD, DESIGNATION) VALUES ('admin', 'admin', '{hash_password('Admin@123')}', 'Admin')",
        f"INSERT INTO USER(USERNAME, NAME, PASSWORD, DESIGNATION) VALUES ('rohan', 'Rohan', '{hash_password('Rohan@123')}', 'CLERK')"
    ]

    for query in insert_data:
        try:
            cur.execute(query)
        except Exception as e:
            print(e)
    con.commit()
    CREATE_DM = True
    print("Tables created successfully")
