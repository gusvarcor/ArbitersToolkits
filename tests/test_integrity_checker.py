"""
Prueba del IntegrityChecker.
"""

from app.engine.sti.fide.integrity_checker import IntegrityChecker
from app.engine.sti.fide.metadata_manager import MetadataManager
import sqlite3

from app.core.config import AppConfig


def main():

    print("=" * 70)
    print("INTEGRITY CHECKER TEST")
    print("=" * 70)
    print()

    # ==========================================================
    # Obtener cantidad real de jugadores
    # ==========================================================

    connection = sqlite3.connect(AppConfig.FIDE_DB)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM players
        """
    )

    total_players = cursor.fetchone()[0]

    connection.close()

    # ==========================================================
    # Actualizar metadata
    # ==========================================================

    metadata = MetadataManager()

    metadata.set("imported_players", total_players)

    metadata.close()

    # ==========================================================
    # Ejecutar verificación
    # ==========================================================

    checker = IntegrityChecker()

    ok, message = checker.check()

    checker.close()

    print("Resultado:")

    if ok:

        print("✅", message)

    else:

        print("❌", message)

    print()


if __name__ == "__main__":
    main()