from PySide6.QtWidgets import QLabel, QStatusBar


class StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()

        self.version_label = QLabel("ArbitersToolkits v0.2.0")
        self.addPermanentWidget(self.version_label)

        self.showMessage("Listo")