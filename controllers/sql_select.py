from dotenv import load_dotenv
import pymysql.cursors
import os
import pandas as pd

load_dotenv()


# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=f'{os.getenv("PASSWORD")}',
    database="dbdatabanco",
    cursorclass=pymysql.cursors.DictCursor,
)


def select_table(table, container):
    """
    Función para seleccionar los datos de una tabla

    Parámetros
    ----------
    table: str
        Nombre de la tabla a seleccionar
    container: container
        Contenedor de opciones
    """
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT * FROM {table}"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
