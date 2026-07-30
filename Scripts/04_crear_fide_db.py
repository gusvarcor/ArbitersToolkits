# ==========================================
# ArbiterTools
# Módulo 4 - Crear Base de Datos FIDE
# ==========================================

import os
import sqlite3
import time
import xml.etree.ElementTree as ET

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.engine.sti.normalizador import (
    normalizar_nombre_fide,
    crear_clave_busqueda,
)

# ------------------------------------------
# Rutas
# ------------------------------------------

RUTA_XML = r"C:\ArbiterTools\BaseFIDE\standard_rating_list.xml"
RUTA_DB = r"C:\ArbiterTools\BaseFIDE\fide.db"

print("=" * 50)
print("ARBITERTOOLS")
print("Creando Base de Datos FIDE")
print("=" * 50)
print()

# ------------------------------------------
# Verificar XML
# ------------------------------------------

if not os.path.exists(RUTA_XML):
    print("ERROR: No se encontró el XML.")
    exit()

print("XML encontrado.")
print()

inicio = time.time()

# ------------------------------------------
# Crear Base de Datos
# ------------------------------------------

conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()

cursor.execute("DROP TABLE IF EXISTS jugadores")

cursor.execute("""
CREATE TABLE jugadores(

    fideid INTEGER PRIMARY KEY,

    nombre TEXT,
    nombre_normalizado TEXT,
    clave_busqueda TEXT,

    pais TEXT,

    sexo TEXT,

    titulo TEXT,
    titulo_w TEXT,
    titulo_o TEXT,
    titulo_foa TEXT,

    elo INTEGER,
    partidas INTEGER,
    k INTEGER,

    nacimiento INTEGER,

    bandera TEXT

)
""")

conexion.commit()

print("Base creada correctamente.")
print()

# ------------------------------------------
# Leer XML
# ------------------------------------------

print("Leyendo XML...")

tree = ET.parse(RUTA_XML)
root = tree.getroot()

contador = 0

# ------------------------------------------
# Importar jugadores
# ------------------------------------------

print("Importando jugadores...")
print()

for jugador in root.findall("player"):

    datos = {}

    for campo in jugador:
        datos[campo.tag] = campo.text

    nombre = datos.get("name") or ""
    nombre_normalizado = normalizar_nombre_fide(nombre)
    clave_busqueda = crear_clave_busqueda(nombre)

    cursor.execute("""
        INSERT INTO jugadores(
            fideid,
            nombre,
            nombre_normalizado,
            clave_busqueda,
            pais,
            sexo,
            titulo,
            titulo_w,
            titulo_o,
            titulo_foa,
            elo,
            partidas,
            k,
            nacimiento,
            bandera
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (

        int(datos.get("fideid", 0)),

        nombre,
        nombre_normalizado,
        clave_busqueda,

        datos.get("country"),

        datos.get("sex"),

        datos.get("title"),
        datos.get("w_title"),
        datos.get("o_title"),
        datos.get("foa_title"),

        int(datos.get("rating") or 0),
        int(datos.get("games") or 0),
        int(datos.get("k") or 0),

        int(datos.get("birthday") or 0),

        datos.get("flag")

    ))

    contador += 1

    if contador % 10000 == 0:
        print(f"{contador:,} jugadores importados...")

conexion.commit()

print()
print("Creando índice de búsqueda...")

cursor.execute("""
CREATE INDEX idx_nombre_normalizado
ON jugadores(nombre_normalizado)
""")

cursor.execute("""
CREATE INDEX idx_clave_busqueda
ON jugadores(clave_busqueda)
""")

conexion.commit()
conexion.close()

fin = time.time()

print()
print("=" * 50)
print("PROCESO TERMINADO")
print("=" * 50)
print()

print(f"Jugadores importados : {contador:,}")
print(f"Tiempo empleado      : {fin - inicio:.2f} segundos")

print()
print("Base de datos creada correctamente.")