"""
Integrity Checker del FIDE Data Engine.

Responsabilidad:

Verificar que la base de datos FIDE sea consistente.
"""

import sqlite3

from app.core.config import AppConfig
from app.engine.sti.fide.metadata_manager import MetadataManager


class IntegrityChecker:

    def __init__(self):

        self.connection = sqlite3.connect(AppConfig.FIDE_DB)
        self.cursor = self.connection.cursor()

    # ==========================================================

    def check(self):

        """
        Ejecuta todas las verificaciones.

        Devuelve:
            (True, "OK") si todo está correcto.
            (False, "mensaje") si encuentra un problema.
        """

        # ------------------------------------------------------
        # Tabla players
        # ------------------------------------------------------

        self.cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name='players'
        """)

        if self.cursor.fetchone() is None:

            return False, "No existe la tabla 'players'."

        # ------------------------------------------------------
        # Tabla metadata
        # ------------------------------------------------------

        self.cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name='metadata'
        """)

        if self.cursor.fetchone() is None:

            return False, "No existe la tabla 'metadata'."

        # ------------------------------------------------------
        # Cantidad real de jugadores
        # ------------------------------------------------------

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM players
        """)

        real_players = self.cursor.fetchone()[0]

        # ------------------------------------------------------
        # Metadata
        # ------------------------------------------------------

        metadata = MetadataManager()

        imported = metadata.get("imported_players")

        metadata.close()

        if imported is None:

            return False, "No existe 'imported_players' en metadata."

        imported = int(imported)

        if imported != real_players:

            return (
                False,
                f"Cantidad distinta. Metadata={imported} SQLite={real_players}"
            )

        return True, "Integridad correcta."

    # ==========================================================

    def close(self):

        self.connection.close()