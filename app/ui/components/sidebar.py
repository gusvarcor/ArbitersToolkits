from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        # Debe coincidir con styles.qss
        self.setObjectName("Sidebar")

        self.setFixedWidth(230)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        title = QLabel("ArbitersToolkits")
        title.setObjectName("sidebarTitle")
        layout.addWidget(title)

        layout.addSpacing(15)

        self.dashboard_btn = QPushButton("🏠 Dashboard")
        self.sti_btn = QPushButton("📥 Smart Tournament Import")
        self.documents_btn = QPushButton("📄 Tournament Documents")
        self.players_btn = QPushButton("👤 Player Database")
        self.validator_btn = QPushButton("✔ Tournament Validator")
        self.payments_btn = QPushButton("💰 Tournament Payments")
        self.statistics_btn = QPushButton("📊 Statistics")
        self.settings_btn = QPushButton("⚙ Settings")

        buttons = [
            self.dashboard_btn,
            self.sti_btn,
            self.documents_btn,
            self.players_btn,
            self.validator_btn,
            self.payments_btn,
            self.statistics_btn,
            self.settings_btn,
        ]

        for button in buttons:
            button.setMinimumHeight(40)
            layout.addWidget(button)

        layout.addStretch()

        self.setLayout(layout)