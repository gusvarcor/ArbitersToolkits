from PySide6.QtWidgets import QStackedWidget

from app.ui.dashboard.dashboard_page import DashboardPage
from app.ui.sti.sti_page import STIPage


class NavigationManager(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.dashboard = DashboardPage()
        self.sti = STIPage()

        self.addWidget(self.dashboard)
        self.addWidget(self.sti)

        self.setCurrentWidget(self.dashboard)

    def show_dashboard(self):
        self.setCurrentWidget(self.dashboard)

    def show_sti(self):
        self.setCurrentWidget(self.sti)