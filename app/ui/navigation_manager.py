from PySide6.QtWidgets import QStackedWidget

from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.sti_page import STIPage


class NavigationManager(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Crear páginas
        self.dashboard = DashboardPage()
        self.sti = STIPage()

        # Agregarlas al contenedor
        self.addWidget(self.dashboard)
        self.addWidget(self.sti)

        # Mostrar Dashboard al iniciar
        self.setCurrentWidget(self.dashboard)

    def show_dashboard(self):
        self.setCurrentWidget(self.dashboard)

    def show_sti(self):
        self.setCurrentWidget(self.sti)