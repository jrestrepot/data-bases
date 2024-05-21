import os

import pandas as pd
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()


# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=f'{os.getenv("PASSWORD")}',
    database="dbdatabanco",
    cursorclass=pymysql.cursors.DictCursor,
)


def update_table(table, container, id, columna, valor):
    """
    Función para seleccionar los datos de una tabla

    Parámetros
    ----------
    table: str
        Nombre de la tabla a seleccionar
    container: container
        Contenedor de opciones
    id: int
        ID del registro a actualizar
    columna: str
        Nombre de la columna a actualizar
    valor: str
        Nuevo valor de la columna
    """
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE {table} SET {columna} = '{valor}' WHERE id = {id}"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
