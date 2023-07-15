import sqlite3
from ..constants.global_constants import DB_NAME

connection = sqlite3.connect('ishop.db')


class SingleConnection(sqlite3.Connection):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the Connection...')
            cls._instance = sqlite3.connect(DB_NAME, check_same_thread=False)
            cls._instance.row_factory = sqlite3.Row
        return cls._instance
