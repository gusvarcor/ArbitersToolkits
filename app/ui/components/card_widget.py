from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class CardWidget(QFrame):
    clicked = Signal()

    def __init__(self, title: str, description: str):
        super().__init__()

        self.setObjectName("CardWidget")

        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.setMinimumSize(240, 150)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("CardTitle")

        self.description_label = QLabel(description)
        self.description_label.setObjectName("CardDescription")
        self.description_label.setWordWrap(True)

        layout.addWidget(self.title_label)
        layout.addWidget(self.description_label)
        layout.addStretch()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

        super().mousePressEvent(event)