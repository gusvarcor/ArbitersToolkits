"""
Prueba del Importer FIDE.

Versión 2

Importa los primeros 100 jugadores y verifica
que quedaron almacenados correctamente.
"""

import sqlite3

from app.core.config import AppConfig
from app.engine.sti.fide.importer import Importer


def main():

    print("=" * 70)
    print("FIDE IMPORTER TEST")
    print("=" * 70)
    print()

    # ==========================================================
    # Limpiar tabla
    # ==========================================================

    connection = sqlite3.connect(AppConfig.FIDE_DB)

    cursor = connection.cursor()

    cursor.execute("DELETE FROM players")

    connection.commit()

    connection.close()

    print("Tabla players limpiada.")
    print()

    # ==========================================================
    # Importar
    # ==========================================================

    importer = Importer(limit=100)

    imported = importer.import_players()

    print(f"Jugadores importados : {imported}")
    print()

    # ==========================================================
    # Verificar cantidad
    # ==========================================================

    connection = sqlite3.connect(AppConfig.FIDE_DB)

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM players")

    total = cursor.fetchone()[0]

    print(f"Jugadores en SQLite : {total}")
    print()

    # ==========================================================
    # Mostrar primeros 10
    # ==========================================================

    cursor.execute("""
        SELECT
            fideid,
            name,
            country,
            rating
        FROM players
        ORDER BY fideid
        LIMIT 10
    """)

    print("=" * 70)
    print("PRIMEROS 10 JUGADORES")
    print("=" * 70)
    print()

    rows = cursor.fetchall()

    for row in rows:

        fideid, name, country, rating = row

        print(
            f"{fideid:<10} "
            f"{country:<4} "
            f"{rating:<5} "
            f"{name}"
        )

    connection.close()

    print()
    print("=" * 70)

    if total == imported:

        print("✅ PRUEBA SUPERADA")

    else:

        print("❌ ERROR EN LA IMPORTACIÓN")

        print(f"Importados : {imported}")

        print(f"SQLite     : {total}")


if __name__ == "__main__":
    main()