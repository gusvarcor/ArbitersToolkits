from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from app.core.config import AppConfig


class WelcomeWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("WelcomeWidget")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        title = QLabel(f"Bienvenido, {AppConfig.USER_NAME}")
        title.setObjectName("DashboardTitle")

        subtitle = QLabel(AppConfig.APP_NAME)
        subtitle.setObjectName("DashboardSubtitle")

        description = QLabel(
            "Professional Chess Tournament Suite\n\n"
            "Selecciona una herramienta del panel izquierdo para comenzar."
        )
        description.setObjectName("DashboardDescription")
        description.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(description)