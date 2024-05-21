import pymysql.cursors
import os


# Conectarse a la base de datos
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password=f'{os.getenv("PASSWORD")}',
        database="dbdatabanco",
        cursorclass=pymysql.cursors.DictCursor,
    )
