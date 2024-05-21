import streamlit as st

from controllers import sql_functions as func

if __name__ == "__main__":
    # Definimos el título de la página y el ícono
    st.set_page_config(
        page_title="Entrega Final Bases de Datos",
        page_icon=":star:",
    )

    st.title("Funciones")

    st.header("Activos")

    nemo = st.text_input("Nemotécnico")

    if st.button("Obtener macroactivo"):
        activos = func.function_activos(nemo)
        st.write(activos)

    st.header("Tasas")

    moneda = st.text_input("Moneda")

    if st.button("Obtener tasa"):
        tasa = func.function_tasa_moneda(moneda)
        st.write(tasa)
