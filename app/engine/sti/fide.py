from app.core.config import AppConfig

# ==========================================
# ArbiterTools
# Librería FIDE
# ==========================================

import sqlite3

from app.engine.sti.normalizador import normalizar_nombre_fide

RUTA_DB = AppConfig.FIDE_DB


def conectar():
    """
    Abre una conexión con la base FIDE.
    """
    return sqlite3.connect(RUTA_DB)


def buscar_por_nombre(nombre, limite=30):
    """
    Busca jugadores cuyo nombre contenga el texto indicado.

    Devuelve una lista de tuplas:
    (fideid, nombre, pais, elo)
    """

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            fideid,
            nombre,
            pais,
            elo
        FROM jugadores
        WHERE nombre LIKE ?
        ORDER BY nombre
        LIMIT ?
    """, (f"%{nombre}%", limite))

    resultados = cursor.fetchall()

    conexion.close()

    return resultados


def buscar_por_apellidos(apellido_paterno, apellido_materno="", limite=30):
    """
    Busca candidatos FIDE utilizando únicamente los apellidos.

    Se normalizan los apellidos para eliminar:
    - acentos
    - ñ
    - diéresis
    - caracteres especiales

    Devuelve:
        (fideid, nombre, pais, elo)
    """

    apellido_paterno = normalizar_nombre_fide(apellido_paterno)
    apellido_materno = normalizar_nombre_fide(apellido_materno)

    texto_busqueda = f"{apellido_paterno} {apellido_materno}".strip()

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            fideid,
            nombre,
            pais,
            elo
        FROM jugadores
        ORDER BY nombre
    """)

    candidatos = []

    for fila in cursor.fetchall():

        nombre_normalizado = normalizar_nombre_fide(fila[1])

        if texto_busqueda in nombre_normalizado:
            candidatos.append(fila)

            if len(candidatos) >= limite:
                break

    conexion.close()

    return candidatos


def buscar_por_id(fideid):
    """
    Busca un jugador por su ID FIDE.
    """

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM jugadores
        WHERE fideid = ?
    """, (fideid,))

    jugador = cursor.fetchone()

    conexion.close()

    return jugador


def buscar_por_nombre_y_nacimiento(nombre, nacimiento=None, limite=20):
    """
    Busca jugadores por nombre y, si se proporciona,
    por año de nacimiento.

    Devuelve:
    (fideid, nombre, pais, elo, nacimiento)
    """

    conexion = conectar()
    cursor = conexion.cursor()

    if nacimiento:

        cursor.execute("""
            SELECT
                fideid,
                nombre,
                pais,
                elo,
                nacimiento
            FROM jugadores
            WHERE nombre LIKE ?
              AND nacimiento = ?
            ORDER BY nombre
            LIMIT ?
        """, (f"%{nombre}%", nacimiento, limite))

    else:

        cursor.execute("""
            SELECT
                fideid,
                nombre,
                pais,
                elo,
                nacimiento
            FROM jugadores
            WHERE nombre LIKE ?
            ORDER BY nombre
            LIMIT ?
        """, (f"%{nombre}%", limite))

    resultados = cursor.fetchall()

    conexion.close()

    return resultados