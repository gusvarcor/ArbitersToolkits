"""
Downloader oficial del FIDE Data Engine.

Responsabilidad:
    - Descargar la lista XML oficial de FIDE.
    - Guardar el ZIP en la carpeta del mes.
    - Extraer el XML.
    - Devolver la ruta del XML.

No valida.

No importa.

No procesa.

Únicamente descarga.
"""

from datetime import datetime
from pathlib import Path
import zipfile

import requests

from app.core.config import AppConfig
from app.core.result import EngineResult


class Downloader:

    def download_latest(self) -> EngineResult:
        """
        Descarga la última lista XML oficial de FIDE.
        """

        try:

            # -------------------------------------------------
            # Crear carpeta del mes
            # -------------------------------------------------

            month_folder = self._create_month_folder()

            zip_path = month_folder / "players_list_xml.zip"

            # -------------------------------------------------
            # Descargar ZIP
            # -------------------------------------------------

            response = requests.get(
                AppConfig.FIDE_COMBINED_XML_URL,
                timeout=120,
                stream=True,
            )

            if response.status_code != 200:

                return EngineResult.fail(
                    f"FIDE respondió con HTTP {response.status_code}."
                )

            with open(zip_path, "wb") as file:

                for chunk in response.iter_content(8192):

                    if chunk:
                        file.write(chunk)

            # -------------------------------------------------
            # Validar ZIP
            # -------------------------------------------------

            if not zipfile.is_zipfile(zip_path):

                return EngineResult.fail(
                    "El archivo descargado no es un ZIP válido."
                )

            # -------------------------------------------------
            # Eliminar XML anteriores
            # -------------------------------------------------

            for xml in month_folder.glob("*.xml"):

                xml.unlink()

            # -------------------------------------------------
            # Extraer ZIP
            # -------------------------------------------------

            with zipfile.ZipFile(zip_path, "r") as zip_file:

                zip_file.extractall(month_folder)

            # -------------------------------------------------
            # Buscar XML
            # -------------------------------------------------

            xml_files = list(month_folder.glob("*.xml"))

            if len(xml_files) == 0:

                return EngineResult.fail(
                    "No se encontró ningún XML dentro del ZIP."
                )

            if len(xml_files) > 1:

                return EngineResult.fail(
                    "Se encontraron múltiples archivos XML."
                )

            return EngineResult.ok(
                message="Lista descargada correctamente.",
                file_path=xml_files[0],
            )

        except requests.exceptions.Timeout:

            return EngineResult.fail(
                "Tiempo de espera agotado al conectar con FIDE."
            )

        except requests.exceptions.ConnectionError:

            return EngineResult.fail(
                "No fue posible conectar con el servidor FIDE."
            )

        except Exception as ex:

            return EngineResult.fail(
                message=str(ex),
                error=ex,
            )

    # ==========================================================
    # Métodos privados
    # ==========================================================

    def _create_month_folder(self) -> Path:
        """
        Crea automáticamente la carpeta correspondiente al mes actual.
        """

        month = datetime.now().strftime("%Y-%m")

        folder = AppConfig.DOWNLOADS_DIR / month

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        return folder