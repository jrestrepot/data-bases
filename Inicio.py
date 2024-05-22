import streamlit as st

# Definimos el título de la página y el ícono
st.set_page_config(
    page_title="Entrega Final Bases de Datos",
    page_icon=":star:",
)

# Título de la página y descripción
st.title("Gestión de datos en el Banco de Inversión Meridian Wealth Management")
st.text(
    "Aplicación conectada a la base de datos del Banco de Inversión Meridian Wealth \nManagement que hace las operaciones de: Insertar, Actualizar, Borrar y consul-\ntar datos, y adicionalmente implementa 2 funciones, 2 triggers y 1 procedimiento."
)
st.image("images/logo_morado.png")
