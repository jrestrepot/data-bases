import pandas as pd
from dotenv import load_dotenv
from utils import get_connection

load_dotenv()


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

    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO {table} VALUES ({', '.join(str.split(valores))})"
            cursor.execute(sql)
            connection.commit()
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
