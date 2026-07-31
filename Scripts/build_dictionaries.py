"""
build_dictionaries.py

Construye los diccionarios utilizados por
Smart Name Intelligence.
"""

import json
import sqlite3
from collections import Counter
from pathlib import Path

from app.engine.sti.sni.text_cleaner import (
    limpiar_palabra,
    palabra_valida,
)


BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "fide.db"

OUTPUT_DIR = BASE_DIR / "data" / "dictionaries"


def main():

    print("=" * 60)
    print("SMART NAME INTELLIGENCE")
    print("CONSTRUCTOR DE DICCIONARIOS")
    print("=" * 60)
    print()

    OUTPUT_DIR.mkdir(exist_ok=True)

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT nombre
        FROM jugadores
        WHERE nombre IS NOT NULL
        """
    )

    contador_nombres = Counter()

    total = 0

    for (nombre_completo,) in cursor:

        total += 1

        if "," not in nombre_completo:
            continue

        try:

            apellidos, nombres = nombre_completo.split(",", 1)

            nombres = nombres.strip()

            for palabra in nombres.split():

                palabra = limpiar_palabra(palabra)

                if not palabra_valida(palabra):
                    continue

                contador_nombres[palabra] += 1

        except Exception:
            continue

        if total % 50000 == 0:

            print(f"{total:,} jugadores procesados...")

    conexion.close()

    nombres_ordenados = dict(
        sorted(
            contador_nombres.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )

    archivo = OUTPUT_DIR / "nombres.json"

    with open(
        archivo,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            nombres_ordenados,
            f,
            indent=4,
            ensure_ascii=False,
        )

    print()
    print("=" * 60)
    print("Proceso terminado")
    print(f"Jugadores procesados : {total:,}")
    print(f"Nombres únicos       : {len(contador_nombres):,}")
    print(f"Archivo generado     : {archivo}")
    print("=" * 60)


if __name__ == "__main__":

    main()