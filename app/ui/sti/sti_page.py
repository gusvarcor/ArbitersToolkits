from PySide6.QtWidgets import QVBoxLayout, QWidget

from app.ui.sti.widgets.import_panel import ImportPanel


class STIPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(24)

        self.import_panel = ImportPanel()

        main_layout.addWidget(self.import_panel)
        main_layout.addStretch()