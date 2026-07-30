"""
nombre_parser.py

Responsabilidad:
Convertir un nombre completo en:

- apellido_paterno
- apellido_materno
- nombres

Versión inicial.
Posteriormente iremos agregando reglas para nombres compuestos,
partículas (de, del, de la, van, von, etc.) y excepciones.
"""

from app.engine.sti.jugador import Jugador


def parsear_nombre(nombre_completo: str) -> Jugador:
    jugador = Jugador()

    if not nombre_completo:
        return jugador

    # Eliminar espacios repetidos
    partes = str(nombre_completo).strip().split()

    if len(partes) == 0:
        return jugador

    # Un solo elemento
    if len(partes) == 1:
        jugador.nombres = partes[0]
        return jugador

    # Dos palabras:
    # Nombre Apellido
    if len(partes) == 2:
        jugador.nombres = partes[0]
        jugador.apellido_paterno = partes[1]
        return jugador

    # Tres palabras:
    # Nombre ApellidoPaterno ApellidoMaterno
    if len(partes) == 3:
        jugador.nombres = partes[0]
        jugador.apellido_paterno = partes[1]
        jugador.apellido_materno = partes[2]
        return jugador

    # Cuatro o más palabras:
    # Nombre(s) + Apellido Paterno + Apellido Materno
    jugador.nombres = " ".join(partes[:-2])
    jugador.apellido_paterno = partes[-2]
    jugador.apellido_materno = partes[-1]

    return jugador