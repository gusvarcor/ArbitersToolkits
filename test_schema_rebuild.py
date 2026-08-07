"""
Prueba de reconstrucción completa de la base FIDE.
"""

from pathlib import Path

from app.core.config import AppConfig
from app.engine.sti.fide.schema_builder import SchemaBuilder


def main():

    print("=" * 70)
    print("SCHEMA REBUILD TEST")
    print("=" * 70)
    print()

    print("Base actual:")

    if AppConfig.FIDE_DB.exists():

        print("SI")

        print(f"Tamaño: {AppConfig.FIDE_DB.stat().st_size:,} bytes")

    else:

        print("NO")

    print()

    builder = SchemaBuilder()

    print("Reconstruyendo base...")

    builder.rebuild_database()

    print("OK")

    print()

    print("Verificando...")

    if AppConfig.FIDE_DB.exists():

        print("Base creada correctamente.")

        print(f"Tamaño: {AppConfig.FIDE_DB.stat().st_size:,} bytes")

    else:

        print("ERROR: No se creó la base.")

    print()

    print("=" * 70)
    print("PRUEBA FINALIZADA")
    print("=" * 70)


if __name__ == "__main__":
    main()