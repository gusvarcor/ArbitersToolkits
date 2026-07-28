import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow
from app.ui.theme import ThemeManager


def main():
    app = QApplication(sys.argv)

    # Cargar el tema visual
    app.setStyleSheet(ThemeManager.load())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()