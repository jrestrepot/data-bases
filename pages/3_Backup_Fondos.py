import os

import streamlit as st
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

if __name__ == "__main__":
    # Definimos el título de la página y el ícono
    st.set_page_config(
        page_title="Entrega Final Bases de Datos",
        page_icon=":star:",
    )

    st.title("Backup de Fondos")

    st.write(
        "En esta sección podrá visualizar un backup de la tabla de Fondos. Para ello, deberá ingresar el nombre del archivo en el que se guardará el backup."
    )

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT * FROM backup_fondos"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            st.dataframe(df)
