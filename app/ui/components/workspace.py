from PySide6.QtWidgets import QFrame, QVBoxLayout

from app.ui.navigation_manager import NavigationManager


class Workspace(QFrame):
    def __init__(self):
        super().__init__()

        # Nombre utilizado por styles.qss
        self.setObjectName("Workspace")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Administrador de navegación
        self.navigation = NavigationManager()

        layout.addWidget(self.navigation)

        self.setLayout(layout)