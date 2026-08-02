"""
SQLite Writer del FIDE Data Engine.

Responsabilidad:

Recibir jugadores y escribirlos en SQLite.

No conoce XML.
"""

import sqlite3

from app.core.config import AppConfig


class SQLiteWriter:

    def __init__(self, batch_size=1000):

        self.batch_size = batch_size

        self.connection = sqlite3.connect(AppConfig.FIDE_DB)

        self.cursor = self.connection.cursor()

        self.buffer = []

    # ==========================================================

    def add(self, player):

        self.buffer.append(self._player_to_tuple(player))

        if len(self.buffer) >= self.batch_size:

            self.flush()

    # ==========================================================

    def flush(self):

        if not self.buffer:
            return

        self.cursor.executemany(
            """
            INSERT OR REPLACE INTO players
            (
                fideid,
                name,
                country,
                sex,
                title,
                w_title,
                o_title,
                foa_title,
                rating,
                games,
                k,
                rapid_rating,
                rapid_games,
                rapid_k,
                blitz_rating,
                blitz_games,
                blitz_k,
                birthday,
                flag
            )
            VALUES
            (
                ?,?,?,?,?,?,?,?,?,?,
                ?,?,?,?,?,?,?,?,?
            )
            """,
            self.buffer,
        )

        self.connection.commit()

        self.buffer.clear()

    # ==========================================================

    def close(self):

        self.flush()

        self.connection.close()

    # ==========================================================

    def _player_to_tuple(self, p):

        return (
            self._to_int(p.get("fideid")),
            p.get("name"),
            p.get("country"),
            p.get("sex"),
            p.get("title"),
            p.get("w_title"),
            p.get("o_title"),
            p.get("foa_title"),
            self._to_int(p.get("rating")),
            self._to_int(p.get("games")),
            self._to_int(p.get("k")),
            self._to_int(p.get("rapid_rating")),
            self._to_int(p.get("rapid_games")),
            self._to_int(p.get("rapid_k")),
            self._to_int(p.get("blitz_rating")),
            self._to_int(p.get("blitz_games")),
            self._to_int(p.get("blitz_k")),
            self._to_int(p.get("birthday")),
            p.get("flag"),
        )

    # ==========================================================

    def _to_int(self, value):

        if value is None:
            return None

        value = value.strip()

        if value == "":
            return None

        try:
            return int(value)

        except ValueError:
            return None