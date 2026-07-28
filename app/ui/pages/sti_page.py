from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class STIPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titulo = QLabel("Smart Tournament Import")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addStretch()

        self.setLayout(layout)