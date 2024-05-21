import os

import pandas as pd
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()


# Conectarse a la base de datos
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=f'{os.getenv("PASSWORD")}',
    database="dbdatabanco",
    cursorclass=pymysql.cursors.DictCursor,
)


def insert_into_table(table, container, valores):
    """
    Función para eliminar los datos de una tabla

    Parámetros
    ----------
    table: str
        Nombre de la tabla a eliminar
    container: container
        Contenedor de opciones
    valores: list
        Lista de valores a insertar
    """

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO {table} VALUES ({', '.join(str.split(valores))})"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
