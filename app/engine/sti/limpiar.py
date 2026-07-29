# ==========================================
# ArbiterTools
# Librería de limpieza de texto
# ==========================================

import unicodedata
import re


def quitar_acentos(texto):
    """
    Elimina acentos, diéresis y convierte Ñ en N.
    """

    if texto is None:
        return ""

    texto = str(texto)

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )

    texto = texto.replace("ñ", "n")
    texto = texto.replace("Ñ", "N")

    return texto


def limpiar_nombre(texto):
    """
    Limpieza estándar utilizada por todo ArbiterTools.
    """

    texto = quitar_acentos(texto)

    texto = texto.strip()

    texto = re.sub(r"\s+", " ", texto)

    return texto.title()


def crear_clave(texto):
    """
    Convierte un nombre en una clave de búsqueda.
    """

    texto = limpiar_nombre(texto)

    texto = texto.lower()

    texto = texto.replace(" ", "")

    texto = texto.replace(",", "")

    return texto