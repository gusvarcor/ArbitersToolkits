from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from app.ui.components.header import Header
from app.ui.components.sidebar import Sidebar
from app.ui.components.status_bar import StatusBar
from app.ui.components.workspace import Workspace


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArbitersToolkits v0.2.0")
        self.resize(1400, 850)

        # Componentes
        self.header = Header()
        self.sidebar = Sidebar()
        self.workspace = Workspace()
        self.status_bar = StatusBar()

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal vertical
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header
        main_layout.addWidget(self.header)

        # Layout horizontal
        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        content_layout.addWidget(self.sidebar)
        content_layout.addWidget(self.workspace)

        main_layout.addLayout(content_layout)

        # Status Bar
        self.setStatusBar(self.status_bar)

        # ==========================
        # Conectar navegación
        # ==========================

        self.sidebar.dashboard_btn.clicked.connect(
            self.workspace.navigation.show_dashboard
        )

        self.sidebar.sti_btn.clicked.connect(
            self.workspace.navigation.show_sti
        )