import os
from urllib.parse import quote_plus

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASS')
DB_URL = os.getenv('DB_URL')
DB_NAME = os.getenv('DB_NAME')

DATABASE_URL = (
    "mssql+pyodbc://{}:{}@{}/{}?driver=ODBC+Driver+17+for+SQL+Server".format(DB_USER,
                                                                             quote_plus(DB_PASSWORD),
                                                                             DB_URL,
                                                                             DB_NAME)
)


PASS_KEY = os.getenv('PASS_KEY')
DEV_MODE = os.getenv('DEV_MODE', False)