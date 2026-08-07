"""
Schema Builder del FIDE Data Engine.

Responsabilidad:

- Crear la base SQLite.
- Crear las tablas.
- Crear índices.

No importa jugadores.
No descarga archivos.
No procesa XML.
"""

import sqlite3

from app.core.config import AppConfig


class SchemaBuilder:

    # ==========================================================
    # Inicialización completa
    # ==========================================================

    def initialize(self):
        """
        Crea la estructura de la base de datos.
        """

        connection = sqlite3.connect(AppConfig.FIDE_DB)

        try:

            self.create_players_table(connection)
            self.create_metadata_table(connection)
            self.create_indexes(connection)

            connection.commit()

        finally:

            connection.close()

    # ==========================================================
    # Reconstrucción completa
    # ==========================================================

    def rebuild_database(self):
        """
        Elimina la base existente y la crea nuevamente.
        """

        if AppConfig.FIDE_DB.exists():

            AppConfig.FIDE_DB.unlink()

        self.initialize()

    # ==========================================================
    # Tabla players
    # ==========================================================

    def create_players_table(self, connection):

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS players (

                fideid INTEGER PRIMARY KEY,

                name TEXT,

                country TEXT,

                sex TEXT,

                title TEXT,

                w_title TEXT,

                o_title TEXT,

                foa_title TEXT,

                rating INTEGER,

                games INTEGER,

                k INTEGER,

                rapid_rating INTEGER,

                rapid_games INTEGER,

                rapid_k INTEGER,

                blitz_rating INTEGER,

                blitz_games INTEGER,

                blitz_k INTEGER,

                birthday INTEGER,

                flag TEXT

            );
            """
        )

    # ==========================================================
    # Tabla metadata
    # ==========================================================

    def create_metadata_table(self, connection):

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS metadata (

                key TEXT PRIMARY KEY,

                value TEXT

            );
            """
        )

    # ==========================================================
    # Índices
    # ==========================================================

    def create_indexes(self, connection):

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_players_name
            ON players(name);
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_players_country
            ON players(country);
            """
        )

        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_players_rating
            ON players(rating);
            """
        )

    # ==========================================================
    # Versión del esquema
    # ==========================================================

    @staticmethod
    def get_schema_version():

        return 1