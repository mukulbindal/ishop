import sqlite3
from ..schema.schemas import User


def login(username):
    connection = sqlite3.connect('ishop.db')
    connection.row_factory = sqlite3.Row
    query = f"select id, username, password, designation from user where username='{username}'"
    cur = connection.cursor()
    cur.execute(query)

    data = cur.fetchone()

    return User(id=data['ID'], username=data['USERNAME'],
                designation=data['DESIGNATION'], password=data['PASSWORD'])
