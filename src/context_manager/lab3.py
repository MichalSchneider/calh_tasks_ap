# lab4
# Napisz manager contextu wspierający operacje na bazie danych w naszym przypadku sqllite
# https://docs.python.org/3/library/sqlite3.html
# /tests/context_manager/test_lab3.py

import sqlite3
from contextlib import contextmanager   # nie wiem czy mogłem użyć tej funkcji ale zainspirowałeem się jednym podobnym rozwiązaniem z internetu


class DB:

    def __init__(self, file_name):

        self.con = sqlite3.connect(file_name)
        self.cursor = self.con.cursor()

@contextmanager
def open_db(file_name: str):

    yield DB(file_name).cursor



