"""
Prueba del SchemaBuilder.

Crea la base de datos SQLite y sus tablas.
"""

import sqlite3

from app.core.config import AppConfig
from app.engine.sti.fide.schema_builder import SchemaBuilder


def main():

    print("=" * 70)
    print("SCHEMA BUILDER TEST")
    print("=" * 70)
    print()

    builder = SchemaBuilder()

    builder.initialize()

    print("✅ Base de datos creada.")
    print()

    print("Ubicación:")

    print(AppConfig.FIDE_DB)

    print()

    connection = sqlite3.connect(AppConfig.FIDE_DB)

    cursor = connection.cursor()

    cursor.execute("""

        SELECT name

        FROM sqlite_master

        WHERE type='table'

        ORDER BY name

    """)

    print("Tablas encontradas")

    print("-" * 70)

    for table in cursor.fetchall():

        print(table[0])

    print()

    cursor.execute("""

        SELECT name

        FROM sqlite_master

        WHERE type='index'

        ORDER BY name

    """)

    print("Índices")

    print("-" * 70)

    for index in cursor.fetchall():

        print(index[0])

    connection.close()


if __name__ == "__main__":
    main()