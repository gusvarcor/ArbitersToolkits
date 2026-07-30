"""
normalizador.py

Motor de normalización de texto para ArbitersToolkits.

Su objetivo es convertir nombres provenientes de distintas fuentes
(FIDE, Chess-Results, Google Forms, Swiss-Manager, etc.) a un formato
comparable.

Todas las búsquedas del proyecto deberán pasar por este módulo.
"""

import re
import unicodedata


def normalizar_nombre_fide(texto: str) -> str:
    """
    Normaliza un nombre para búsquedas tipo FIDE.

    Ejemplos:

    Peña Gómez, José Ángel
        ->
    pena gomez jose angel

    Müller, Günther
        ->
    muller gunther

    Wesley Kwan
        ->
    wesley kwan
    """

    if texto is None:
        return ""

    texto = str(texto).strip()

    if texto == "":
        return ""

    # Caracteres que unicodedata no convierte correctamente
    reemplazos = {
        "ß": "ss",
        "Æ": "AE",
        "æ": "ae",
        "Œ": "OE",
        "œ": "oe",
        "Ø": "O",
        "ø": "o",
        "Ł": "L",
        "ł": "l",
    }

    for origen, destino in reemplazos.items():
        texto = texto.replace(origen, destino)

    # Elimina acentos, diéresis, tildes y convierte Ñ -> N
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ASCII", "ignore").decode("ASCII")

    texto = texto.lower()

    # Sustituir puntuación por espacios
    texto = re.sub(r"[.,;:/\\()\-_'`\"]", " ", texto)

    # Eliminar cualquier otro símbolo extraño
    texto = re.sub(r"[^a-z0-9 ]", " ", texto)

    # Eliminar espacios repetidos
    texto = " ".join(texto.split())

    return texto


def normalizar_apellidos(apellido_paterno: str,
                          apellido_materno: str) -> str:
    """
    Devuelve los apellidos normalizados.

    Ejemplo:

    Ramírez
    Morales

    ->
    ramirez morales
    """

    return normalizar_nombre_fide(
        f"{apellido_paterno} {apellido_materno}"
    )


def crear_clave_busqueda(texto: str) -> str:
    """
    Crea una clave compacta para comparaciones.

    Ejemplo:

    Peña Gómez, José Ángel

    ->
    penagomezjoseangel
    """

    return normalizar_nombre_fide(texto).replace(" ", "")