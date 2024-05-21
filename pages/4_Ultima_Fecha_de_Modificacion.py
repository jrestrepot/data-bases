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
        page_icon=":nauseated_face:",
    )

    st.title("Última Fecha de Modificación")

    st.write(
        "En esta sección podrá visualizar la última fecha de modificación de la base de datos."
    )

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT * FROM ultima_fecha_modificacion"
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            st.dataframe(df)
