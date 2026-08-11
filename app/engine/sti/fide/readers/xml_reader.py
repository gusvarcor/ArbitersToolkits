"""
XML Reader del FIDE Data Engine.

Responsabilidad:

Leer el XML oficial de la FIDE y producir
jugadores uno por uno.

No conoce SQLite.
"""

from pathlib import Path
from lxml import etree
import time

from app.core.config import AppConfig


class XMLReader:

    def __init__(
        self,
        xml_file=None,
        limit=None,
        progress_interval=10000
    ):

        self.xml_file = xml_file
        self.limit = limit
        self.progress_interval = progress_interval

    # ==========================================================

    def __iter__(self):

        xml_path = self._get_xml_path()

        print(
            f"XML: {xml_path}",
            flush=True
        )

        start_time = time.perf_counter()

        context = etree.iterparse(
            str(xml_path),
            events=("end",),
            tag="player"
        )

        count = 0

        try:

            for _, player in context:

                yield self._parse_player(player)

                count += 1

                if (
                    self.progress_interval
                    and count % self.progress_interval == 0
                ):

                    elapsed = (
                        time.perf_counter() - start_time
                    )

                    rate = (
                        count / elapsed
                        if elapsed > 0
                        else 0
                    )

                    print(
                        f"XML procesados: "
                        f"{count:,} "
                        f"| {rate:,.0f} jugadores/s",
                        flush=True
                    )

                player.clear()

                while player.getprevious() is not None:

                    del player.getparent()[0]

                if (
                    self.limit is not None
                    and count >= self.limit
                ):

                    break

        finally:

            del context

            elapsed = (
                time.perf_counter() - start_time
            )

            rate = (
                count / elapsed
                if elapsed > 0
                else 0
            )

            print(
                f"XML finalizado: "
                f"{count:,} jugadores "
                f"| {elapsed:.2f} segundos "
                f"| {rate:,.0f} jugadores/s",
                flush=True
            )

    # ==========================================================

    def _get_xml_path(self):

        #
        # Si el UpdateEngine proporciona un XML,
        # utilizarlo directamente.
        #

        if self.xml_file is not None:

            xml_path = Path(self.xml_file)

            if not xml_path.exists():

                raise FileNotFoundError(xml_path)

            return xml_path

        #
        # Compatibilidad con el comportamiento anterior.
        #

        for folder in sorted(
            AppConfig.DOWNLOADS_DIR.iterdir(),
            reverse=True,
        ):

            if folder.is_dir():

                files = list(
                    folder.glob("*.xml")
                )

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