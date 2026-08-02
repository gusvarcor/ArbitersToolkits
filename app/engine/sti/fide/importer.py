"""
Importer del FIDE Data Engine.

Responsabilidad:

Coordinar la importación entre
XMLReader y SQLiteWriter.

No conoce XML.
No conoce SQLite.
"""

from app.engine.sti.fide.readers.xml_reader import XMLReader
from app.engine.sti.fide.writers.sqlite_writer import SQLiteWriter


class Importer:

    def __init__(self, limit=None, batch_size=1000):

        self.limit = limit
        self.batch_size = batch_size

    # ==========================================================

    def import_players(self):

        reader = XMLReader(limit=self.limit)

        writer = SQLiteWriter(batch_size=self.batch_size)

        imported = 0

        try:

            for player in reader:

                writer.add(player)

                imported += 1

        finally:

            writer.close()

        return imported