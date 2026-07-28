from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel


class Header(QFrame):
    def __init__(self):
        super().__init__()

        # Nombre utilizado por styles.qss
        self.setObjectName("Header")

        layout = QHBoxLayout()

        layout.setContentsMargins(20, 10, 20, 10)

        title = QLabel("ArbitersToolkits")
        title.setObjectName("headerTitle")

        subtitle = QLabel("Professional Chess Tournament Suite")
        subtitle.setObjectName("headerSubtitle")

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(
            subtitle,
            alignment=Qt.AlignmentFlag.AlignRight
        )

        self.setLayout(layout)