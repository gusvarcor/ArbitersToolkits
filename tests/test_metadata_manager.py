"""
Prueba del MetadataManager.
"""

from app.engine.sti.fide.metadata_manager import MetadataManager


def main():

    print("=" * 70)
    print("METADATA MANAGER TEST")
    print("=" * 70)
    print()

    metadata = MetadataManager()

    # ==========================================================
    # Escribir datos
    # ==========================================================

    metadata.set("schema_version", "1")

    metadata.set("fide_list", "2026-08")

    metadata.set("importer_version", "1.0")

    metadata.set("imported_players", "100")

    print("Metadatos escritos.")
    print()

    # ==========================================================
    # Leer un dato
    # ==========================================================

    print("Versión del esquema:")

    print(metadata.get("schema_version"))

    print()

    # ==========================================================
    # Leer todos
    # ==========================================================

    print("=" * 70)

    print("TODOS LOS METADATOS")

    print("=" * 70)

    print()

    data = metadata.get_all()

    for key, value in data.items():

        print(f"{key:<20} {value}")

    metadata.close()


if __name__ == "__main__":
    main()