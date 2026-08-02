"""
Configuración global de ArbitersToolkits.
"""

from pathlib import Path


class AppConfig:

    # ==========================================================
    # Información general
    # ==========================================================

    APP_NAME = "ArbitersToolkits"
    APP_VERSION = "0.4.0-alpha1"
    ORGANIZATION = "ArbitersToolkits"

    # ==========================================================
    # Usuario
    # ==========================================================

    USER_NAME = "Gustavo"

    # ==========================================================
    # Configuración
    # ==========================================================

    LANGUAGE = "es"
    THEME = "dark"

    CURRENT_PROJECT = None

    # ==========================================================
    # Directorios
    # ==========================================================

    BASE_DIR = Path(__file__).resolve().parents[2]

    DATA_DIR = BASE_DIR / "data"

    DOWNLOADS_DIR = DATA_DIR / "downloads"

    SQLITE_DIR = DATA_DIR / "sqlite"

    DICTIONARIES_DIR = DATA_DIR / "dictionaries"

    STATISTICS_DIR = DATA_DIR / "statistics"

    ARCHIVE_DIR = SQLITE_DIR / "archive"

    # ==========================================================
    # Bases de datos
    # ==========================================================

    FIDE_DB = SQLITE_DIR / "fide.db"

    SNI_DB = SQLITE_DIR / "sni.db"

    TOURNAMENT_DB = SQLITE_DIR / "tournaments.db"

    # ==========================================================
    # URLs oficiales
    # ==========================================================

    FIDE_COMBINED_XML_URL = (
        "https://ratings.fide.com/download/players_list_xml.zip"
    )