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


def function_activos(nemo):
    """
    Función para obtener el macroactivo correspondiente a un nemotecnico

    Parámetros
    ----------
    nemo: str
        Nemotecnico
    """

    with connection.cursor() as cursor:
        # Read a single record
        sql = f"SELECT macroactivo_x_nemo('{nemo}')"
        cursor.execute(sql)
        activos = cursor.fetchall()

    return pd.DataFrame(activos)


def function_tasa_moneda(moneda):
    """
    Función para obtener la tasa de una moneda

    Parámetros
    ----------
    moneda: str
        Moneda

    Retornos
    --------
    tasa: pd.DataFrame
        Tasa de la moneda
    """

    with connection.cursor() as cursor:
        # Read a single record
        sql = f"SELECT tasa_moneda('{moneda}')"
        cursor.execute(sql)
        tasa = cursor.fetchall()

    return pd.DataFrame(tasa)
