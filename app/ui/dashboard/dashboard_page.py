from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QWidget,
)

from app.core.config import AppConfig
from app.ui.components.card_widget import CardWidget


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(24)

        # Encabezado
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

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)
        main_layout.addWidget(description)

        # Tarjetas principales
        cards_layout = QGridLayout()
        cards_layout.setHorizontalSpacing(20)
        cards_layout.setVerticalSpacing(20)

        cards_layout.addWidget(
            CardWidget(
                "📥 Smart Tournament Import",
                "Importa torneos desde Chess-Results y Swiss-Manager."
            ),
            0, 0
        )

        cards_layout.addWidget(
            CardWidget(
                "📄 Tournament Documents",
                "Genera documentos y formatos para tus torneos."
            ),
            0, 1
        )

        cards_layout.addWidget(
            CardWidget(
                "👥 Player Database",
                "Consulta y administra la base de datos de jugadores."
            ),
            1, 0
        )

        cards_layout.addWidget(
            CardWidget(
                "✔ Tournament Validator",
                "Verifica que un torneo cumpla con los requisitos FIDE."
            ),
            1, 1
        )

        main_layout.addLayout(cards_layout)
        main_layout.addStretch()