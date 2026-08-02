"""
Metadata Manager del FIDE Data Engine.

Responsabilidad:

Leer y escribir la tabla metadata.
"""

import sqlite3

from app.core.config import AppConfig


class MetadataManager:

    def __init__(self):

        self.connection = sqlite3.connect(AppConfig.FIDE_DB)

        self.cursor = self.connection.cursor()

    # ==========================================================

    def set(self, key, value):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO metadata
            (key, value)
            VALUES (?, ?)
            """,
            (key, str(value)),
        )

        self.connection.commit()

    # ==========================================================

    def get(self, key):

        self.cursor.execute(
            """
            SELECT value
            FROM metadata
            WHERE key = ?
            """,
            (key,),
        )

        row = self.cursor.fetchone()

        if row is None:
            return None

        return row[0]

    # ==========================================================

    def get_all(self):

        self.cursor.execute(
            """
            SELECT key, value
            FROM metadata
            ORDER BY key
            """
        )

        return dict(self.cursor.fetchall())

    # ==========================================================

    def close(self):

        self.connection.close()