import pandas as pd
from dotenv import load_dotenv
from utils import get_connection

load_dotenv()

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
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"DELETE FROM {table} WHERE id = {id}"
            cursor.execute(sql)
            connection.commit()
            # Fetch the result to show updated state
            cursor.execute(f"SELECT * FROM {table}")
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
    finally:
        connection.close()

def delete_last_record(tabla_seleccionada, container):
    """
    Función para eliminar el último dato de la tabla

    Parámetros
    ----------
    tabla_seleccionada: str
        Nombre de la tabla seleccionada
    container: container
        Contenedor de opciones
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"CALL eliminar_ultimo_registro('{tabla_seleccionada}')"
            cursor.execute(sql)
            connection.commit()
            # Fetch the result to show updated state
            cursor.execute(f"SELECT * FROM {tabla_seleccionada}")
            connection.commit()
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
    finally:
        connection.close()
