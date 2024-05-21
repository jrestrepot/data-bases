
import pandas as pd
from utils import get_connection
from dotenv import load_dotenv

load_dotenv()


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

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE {table} SET {columna} = '{valor}' WHERE id = {id}"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
    finally:
        connection.close()
