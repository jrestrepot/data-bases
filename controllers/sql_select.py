from dotenv import load_dotenv
import pymysql.cursors
import os
import pandas as pd

load_dotenv()


# Conectarse a la base de datos
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=f'{os.getenv("PASSWORD")}',
    database="dbdatabanco",
    cursorclass=pymysql.cursors.DictCursor,
)


def select_from_table(table, container, columnas, condicion, orden):
    """
    Función para seleccionar los datos de una tabla

    Parámetros
    ----------
    table: str
        Nombre de la tabla a seleccionar
    container: container
        Contenedor de opciones
    columnas: list
        Lista de columnas a seleccionar
    condicion: str
        Condición de selección
    orden: str
        Orden de selección
    """

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            if columnas:
                sql = f"SELECT {', '.join(str.split(columnas))} FROM {table}"
            else:
                sql = f"SELECT * FROM {table}"
            if condicion:
                sql += f" WHERE {condicion}"
            if orden:
                sql += f" ORDER BY {orden}"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
