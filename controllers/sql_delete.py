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


def delete_from_table(table, container, id):
    """
    Función para eliminar los datos de una tabla

    Parámetros
    ----------
    table: str
        Nombre de la tabla a eliminar
    container: container
        Contenedor de opciones
    id: int
        ID del registro a eliminar
    """

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"DELETE FROM {table} WHERE id = {id}"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)


def delete_last_record(tabla_seleccionada, container):
    """
    Función para eliminar el último dato de la tabla

    Parámetros
    ----------}
    tabla_seleccionada: str
        Nombre de la tabla seleccionada
    container: container
        Contenedor de opciones
    """

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"CALL eliminar_ultimo_registro({tabla_seleccionada})"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
