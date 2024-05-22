import streamlit as st

from controllers import sql_delete, sql_insert, sql_select, sql_update


def crear_container_opciones(
    tabla_seleccionada, consulta_seleccionada, container_opciones, **kwargs
):
    """
    Función para crear el contenedor de opciones

    Parámetros
    ----------
    tabla_seleccionada: str
        Nombre de la tabla seleccionada
    consulta_seleccionada: str
        Nombre de la consulta seleccionada
    container_opciones: container
        Contenedor de opciones
    kwargs: dict
        Argumentos de la consulta

    Retornos
    --------
    container_opciones: container
        Contenedor de opciones
    """

    if consulta_seleccionada == "Seleccionar":
        sql_select.select_from_table(tabla_seleccionada, container_opciones, **kwargs)
    if consulta_seleccionada == "Insertar":
        sql_insert.insert_into_table(tabla_seleccionada, container_opciones, **kwargs)
    if consulta_seleccionada == "Actualizar":
        sql_update.update_table(tabla_seleccionada, container_opciones, **kwargs)
    if consulta_seleccionada == "Eliminar":
        sql_delete.delete_from_table(tabla_seleccionada, container_opciones, **kwargs)
    if consulta_seleccionada == "Eliminar último registro":
        sql_delete.delete_last_record(tabla_seleccionada, container_opciones)


if __name__ == "__main__":
    # Definimos el título de la página y el ícono
    st.set_page_config(
        page_title="Entrega Final Bases de Datos",
        page_icon=":star:",
    )

    opciones_tablas = ["activo", "fondo", "moneda"]
    opciones_consultas = [
        "Seleccionar",
        "Insertar",
        "Actualizar",
        "Eliminar",
        "Eliminar último registro",
    ]

    col1, col2, col3 = st.columns(3)

    container_opciones = st.container()

    with col1:
        tabla_seleccionada = st.selectbox("Seleccione una tabla", opciones_tablas)
        boton_continuar = st.button("Continuar")

    with col2:
        operacion_seleccionada = st.selectbox("Indique la consulta", opciones_consultas)

    with col3:
        argumentos = {}
        if operacion_seleccionada == "Actualizar":
            argumentos["id"] = st.text_input("Indique el id a actualizar")
            argumentos["columna"] = st.text_input("Indique la columna a actualizar")
            argumentos["valor"] = st.text_input("Indique el nuevo valor")
        if operacion_seleccionada == "Eliminar":
            argumentos["id"] = st.text_input("Indique el id a eliminar")
        if operacion_seleccionada == "Insertar":
            argumentos["columnas"] = st.text_input("Indique las columnas a insertar")
            argumentos["valores"] = st.text_input("Indique los valores a insertar")
        if operacion_seleccionada == "Seleccionar":
            argumentos["columnas"] = st.text_input("Indique las columnas a seleccionar")
            argumentos["condicion"] = st.text_input("Indique la condición")
            argumentos["orden"] = st.text_input("Indique el orden")

    if boton_continuar:
        if tabla_seleccionada != None and operacion_seleccionada != None:
            st.write(
                f"Realizando operación {operacion_seleccionada} en la tabla {tabla_seleccionada}..."
            )
            crear_container_opciones(
                tabla_seleccionada,
                operacion_seleccionada,
                container_opciones,
                **argumentos,
            )
        else:
            st.warning("Debe seleccionar una tabla y una consulta para continuar.")
