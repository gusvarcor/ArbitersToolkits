"""
nombre_parser.py

Motor de interpretación de nombres del STI.

A partir del Sprint 13 el parser soporta distintos
formatos de nombres.
"""

from app.engine.sti.jugador import Jugador

from app.engine.sti.nombre_formatos import (
    NOMBRES_APELLIDOS,
    APELLIDOS_NOMBRES,
    AUTOMATICO,
)


def parsear_nombre(
    nombre_completo: str,
    formato=AUTOMATICO
) -> Jugador:

    jugador = Jugador()

    if not nombre_completo:
        return jugador

    partes = str(nombre_completo).strip().split()

    if len(partes) == 0:
        return jugador

    # -----------------------------
    # Un solo elemento
    # -----------------------------

    if len(partes) == 1:
        jugador.nombres = partes[0]
        return jugador

    # -----------------------------
    # Formato:
    #
    # Juan Carlos Perez Lopez
    # -----------------------------

    if formato == NOMBRES_APELLIDOS:

        if len(partes) == 2:
            jugador.nombres = partes[0]
            jugador.apellido_paterno = partes[1]
            return jugador

        if len(partes) == 3:
            jugador.nombres = partes[0]
            jugador.apellido_paterno = partes[1]
            jugador.apellido_materno = partes[2]
            return jugador

        jugador.nombres = " ".join(partes[:-2])
        jugador.apellido_paterno = partes[-2]
        jugador.apellido_materno = partes[-1]

        return jugador

    # -----------------------------
    # Formato:
    #
    # Perez Lopez Juan Carlos
    # -----------------------------

    if formato == APELLIDOS_NOMBRES:

        if len(partes) == 2:
            jugador.apellido_paterno = partes[0]
            jugador.nombres = partes[1]
            return jugador

        if len(partes) == 3:
            jugador.apellido_paterno = partes[0]
            jugador.apellido_materno = partes[1]
            jugador.nombres = partes[2]
            return jugador

        jugador.apellido_paterno = partes[0]
        jugador.apellido_materno = partes[1]
        jugador.nombres = " ".join(partes[2:])

        return jugador

    # -----------------------------
    # AUTOMÁTICO
    #
    # Por ahora conserva el
    # comportamiento anterior.
    # -----------------------------

    if len(partes) == 2:
        jugador.nombres = partes[0]
        jugador.apellido_paterno = partes[1]
        return jugador

    if len(partes) == 3:
        jugador.nombres = partes[0]
        jugador.apellido_paterno = partes[1]
        jugador.apellido_materno = partes[2]
        return jugador

    jugador.nombres = " ".join(partes[:-2])
    jugador.apellido_paterno = partes[-2]
    jugador.apellido_materno = partes[-1]

    return jugador