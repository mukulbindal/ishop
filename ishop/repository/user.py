from ..schema.schemas import User
from ..exceptions.IshopExceptions import NoDataFoundError
from ..utils.connection import SingleConnection


def login(username):
    connection = SingleConnection()
    query = f"select id, username, password, designation from user where username='{username}'"
    cur = connection.cursor()
    cur.execute(query)

    data = cur.fetchone()
    if not data:
        raise NoDataFoundError()
    return User(id=data['ID'], username=data['USERNAME'],
                designation=data['DESIGNATION'], password=data['PASSWORD'])
