import sqlite3
from util import FERNET


class User:
    def __init__(self, name, password, level):
        self.name = name
        self.password = password
        self.level = level
