import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Database():
    location = os.path.join(BASE_DIR, 'db.sqlite3')
    # location = 'http://138.197.169.179/db.sqlite3'
