"""
XML Reader del FIDE Data Engine.

Responsabilidad:

Leer el XML oficial de la FIDE y producir
jugadores uno por uno.

No conoce SQLite.
"""

from lxml import etree

from app.core.config import AppConfig


class XMLReader:

    def __init__(self, limit=None):

        self.limit = limit

    # ==========================================================

    def __iter__(self):

        xml_path = self._get_xml_path()

        context = etree.iterparse(
            str(xml_path),
            events=("end",),
            tag="player",
        )

        count = 0

        try:

            for _, player in context:

                yield self._parse_player(player)

                count += 1

                player.clear()

                while player.getprevious() is not None:
                    del player.getparent()[0]

                if self.limit is not None and count >= self.limit:
                    break

        finally:

            del context

    # ==========================================================

    def _get_xml_path(self):

        for folder in sorted(
            AppConfig.DOWNLOADS_DIR.iterdir(),
            reverse=True
        ):

            if folder.is_dir():

                files = list(folder.glob("*.xml"))

                if files:

                    return files[0]

        raise FileNotFoundError(
            "No se encontró ningún XML FIDE."
        )

    # ==========================================================

    def _parse_player(self, player):

        data = {}

        for child in player:

            value = child.text

            if value is None:
                value = ""

            data[child.tag] = value

        return data