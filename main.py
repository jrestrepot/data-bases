import streamlit

import streamlit.web.cli as stcli
import os, sys


def resolve_path(path):
    """
    Función para resolver la ruta de un archivo o carpeta

    Parámetros
    ----------
    path: str
        Ruta del archivo o carpeta a resolver

    Retornos
    --------
    resolved_path: str
        Ruta resuelta del archivo o carpeta
    """

    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("Inicio.py"),
        # "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
