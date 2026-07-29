"""
Configuración global de ArbitersToolkits.

Este módulo centraliza la configuración general de la aplicación.
En el futuro leerá y guardará estos datos desde un archivo JSON o una
base de datos, pero por ahora utilizaremos valores por defecto.
"""

from pathlib import Path


class AppConfig:
    # ==========================================================
    # Información de la aplicación
    # ==========================================================

    APP_NAME = "ArbitersToolkits"
    APP_VERSION = "0.4.0-alpha1"

    ORGANIZATION = "ArbitersToolkits"

    # ==========================================================
    # Usuario
    # ==========================================================

    USER_NAME = "Gustavo"

    # ==========================================================
    # Configuración general
    # ==========================================================

    LANGUAGE = "es"
    THEME = "dark"

    CURRENT_PROJECT = None

    # ==========================================================
    # Rutas del proyecto
    # ==========================================================

    # Carpeta raíz del proyecto
    BASE_DIR = Path(__file__).resolve().parents[2]

    # Carpeta donde vivirán todos los datos
    DATA_DIR = BASE_DIR / "data"

    # Base de datos FIDE
    FIDE_DB = DATA_DIR / "fide.db"