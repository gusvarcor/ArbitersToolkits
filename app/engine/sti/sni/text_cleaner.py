"""
text_cleaner.py

Utilidades para limpiar palabras utilizadas
por Smart Name Intelligence.
"""

import re


# Palabras que no deben considerarse nombres
PALABRAS_PROHIBIDAS = {

    "dr",
    "mr",
    "mrs",
    "ms",
    "prof",
    "professor",

    "gm",
    "wgm",
    "im",
    "wim",
    "fm",
    "wfm",
    "cm",
    "wcm",

    "ii",
    "iii",
    "iv",
    "jr",
    "sr",

}


def limpiar_palabra(texto: str) -> str:
    """
    Limpia una palabra individual.
    """

    texto = texto.lower()

    texto = texto.replace(".", "")

    texto = texto.strip()

    return texto


def palabra_valida(texto: str) -> bool:
    """
    Determina si una palabra puede
    formar parte de un nombre.
    """

    texto = limpiar_palabra(texto)

    if not texto:
        return False

    # Longitud mínima

    if len(texto) < 2:
        return False

    # Solo letras

    if not re.fullmatch(r"[a-záéíóúüñ'-]+", texto):
        return False

    # Palabras prohibidas

    if texto in PALABRAS_PROHIBIDAS:
        return False

    return True