import cx_Oracle
from config import config

def get_connection():
    return cx_Oracle.connect(config.DB_USER, config.DB_PASSWORD, config.DB_DSN)

