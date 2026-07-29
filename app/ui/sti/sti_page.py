from PySide6.QtWidgets import QVBoxLayout, QWidget

from app.ui.sti.widgets.import_panel import ImportPanel
from app.ui.sti.widgets.player_table import PlayerTable


class STIPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.import_panel = ImportPanel()

        self.player_table = PlayerTable()

        layout.addWidget(self.import_panel)

        layout.addWidget(self.player_table)

        layout.addStretch()

        # Conectar ambos widgets

        self.import_panel.jugadores_importados.connect(
            self.player_table.cargar_jugadores
        )