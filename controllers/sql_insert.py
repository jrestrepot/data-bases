import pandas as pd
from dotenv import load_dotenv
from utils import get_connection

load_dotenv()


def insert_into_table(table, container, columnas, valores):
    """
    Función para eliminar los datos de una tabla

    Parámetros
    ----------
    table: str
        Nombre de la tabla a eliminar
    container: container
        Contenedor de opciones
    columnas: str
        Lista de columnas a insertar
    valores: str
        Lista de valores a insertar
    """

    connection = get_connection()
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            aux = str.split(columnas) + str.split(valores)
            print(aux)
            if columnas:
                print(str.split(columnas))
                print(
                    f"INSERT INTO {table}({', '.join(str.split(columnas))}) VALUES({', '.join(str.split(valores))})"
                )
                sql = f"INSERT INTO {table}({', '.join(str.split(columnas))}) VALUES({', '.join(str.split(valores))})"

            else:
                sql = f"INSERT INTO {table} VALUES({', '.join(str.split(valores))})"
            cursor.execute(sql)
            connection.commit()
            cursor.execute(f"SELECT * FROM {table}")
            df = pd.DataFrame(cursor.fetchall())
            container.dataframe(df)
