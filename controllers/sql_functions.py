import pandas as pd
from dotenv import load_dotenv
from utils import get_connection
load_dotenv()


def function_activos(nemo):
    """
    Función para obtener el macroactivo correspondiente a un nemotecnico

    Parámetros
    ----------
    nemo: str
        Nemotecnico
    """

    connection = get_connection()
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

    connection = get_connection()
    with connection.cursor() as cursor:
        # Read a single record
        sql = f"SELECT tasa_x_moneda('{moneda}')"
        cursor.execute(sql)
        tasa = cursor.fetchall()

    return pd.DataFrame(tasa)
