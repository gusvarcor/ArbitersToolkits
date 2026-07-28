from pathlib import Path


class ThemeManager:
    """
    Administra el tema visual de ArbitersToolkits.
    """

    @staticmethod
    def load() -> str:
        """
        Carga el archivo styles.qss y devuelve su contenido.
        """

        style_file = (
            Path(__file__).parent
            / "resources"
            / "styles"
            / "styles.qss"
        )

        if style_file.exists():
            return style_file.read_text(encoding="utf-8")

        return ""