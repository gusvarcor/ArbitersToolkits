"""
comparador.py

Motor de comparación de nombres para el Smart Tournament Import (STI).

Responsabilidades:

- Normalizar nombres.
- Calcular similitud.
- Elegir el mejor candidato FIDE.
"""

from rapidfuzz import fuzz

from app.engine.sti.limpiar import quitar_acentos


def normalizar(nombre: str) -> str:
    """
    Convierte un nombre a un formato comparable.

    Ejemplo:

    'Ramírez Morales, José Manuel'

    →

    'ramirez morales jose manuel'
    """

    if not nombre:
        return ""

    nombre = quitar_acentos(nombre)

    nombre = nombre.lower()

    nombre = nombre.replace(",", " ")

    nombre = " ".join(nombre.split())

    return nombre


def similitud(nombre1: str, nombre2: str) -> int:
    """
    Devuelve un porcentaje de similitud (0-100).
    """

    return round(
        fuzz.token_sort_ratio(
            normalizar(nombre1),
            normalizar(nombre2)
        )
    )


def comparar(jugador, candidatos):
    """
    Busca el mejor candidato FIDE para un jugador.

    Parámetros
    ----------
    jugador : Jugador

    candidatos : list
        Lista devuelta por buscar_por_nombre()

    Devuelve
    --------
    dict
    """

    nombre_jugador = (
        f"{jugador.apellido_paterno} "
        f"{jugador.apellido_materno}, "
        f"{jugador.nombres}"
    )

    mejor = None
    mejor_puntaje = -1

    for candidato in candidatos:

        fideid, nombre_fide, pais, elo = candidato

        puntos = similitud(
            nombre_jugador,
            nombre_fide
        )

        if puntos > mejor_puntaje:

            mejor_puntaje = puntos
            mejor = candidato

    return {
        "mejor": mejor,
        "confianza": mejor_puntaje,
        "encontrado": mejor is not None
    }