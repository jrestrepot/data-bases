import streamlit as st

from controllers import sql_select, sql_insert, sql_update, sql_delete


def crear_container_opciones(
    tabla_seleccionada, consulta_seleccionada, container_opciones
):
    """
    Función para crear el contenedor de opciones

    Parámetros
    ----------
    tabla_seleccionada: str
        Nombre de la tabla seleccionada
    consulta_seleccionada: str
        Nombre de la consulta seleccionada

    Retornos
    --------
    container_opciones: container
        Contenedor de opciones
    """
    if consulta_seleccionada == "Seleccionar":
        sql_select.select_table(tabla_seleccionada, container_opciones)


if __name__ == "__main__":
    # Definimos el título de la página y el ícono
    st.set_page_config(
        page_title="Entrega Final Bases de Datos",
        page_icon=":nauseated_face:",
    )

    opciones_tablas = ["Activos", "Fondos", "Bolsas", "Monedas"]
    opciones_consultas = ["Seleccionar", "Insertar", "Actualizar", "Eliminar"]

    col1, col2 = st.columns(2)

    container_opciones = st.container()

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
