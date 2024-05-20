import streamlit as st

# Definimos el título de la página y el ícono
st.set_page_config(
    page_title="Entrega Final Bases de Datos",
    page_icon=":nauseated_face:",
)

opciones_tablas = ["Activos", "Fondos", "Bolsas", "Monedas"]
opciones_consultas = ["Seleccionar", "Insertar", "Actualizar", "Eliminar"]

col1, col2 = st.columns(2)

with col1:
    tabla_seleccionada = st.selectbox("Seleccione una tabla", opciones_tablas)
    boton_continuar = st.button("Continuar")

with col2:
    consulta_seleccionada = st.selectbox("Indique la consulta", opciones_consultas)

if boton_continuar:
    if tabla_seleccionada != None and consulta_seleccionada != None:
        st.write(
            f"Realizando consulta {consulta_seleccionada} en la tabla {tabla_seleccionada}..."
        )
    else:
        st.warning("Debe seleccionar una tabla y una consulta para continuar.")
