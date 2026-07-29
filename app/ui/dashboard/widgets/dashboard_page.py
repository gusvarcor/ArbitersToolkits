from PySide6.QtWidgets import (
    QGridLayout,
    QVBoxLayout,
    QWidget,
)

from app.ui.components.card_widget import CardWidget
from app.ui.dashboard.widgets.welcome_widget import WelcomeWidget


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(24)

        # Widget de bienvenida
        main_layout.addWidget(WelcomeWidget())

        # Tarjetas principales
        cards_layout = QGridLayout()
        cards_layout.setHorizontalSpacing(20)
        cards_layout.setVerticalSpacing(20)

        cards_layout.addWidget(
            CardWidget(
                "📥 Smart Tournament Import",
                "Convierte listas de jugadores desde Word, Excel, PDF, CSV y texto a XML compatible con programas de emparejamiento."
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
                "Detecta inconsistencias y valida que el torneo cumpla con los requisitos FIDE."
            ),
            1, 1
        )

        main_layout.addLayout(cards_layout)
        main_layout.addStretch()