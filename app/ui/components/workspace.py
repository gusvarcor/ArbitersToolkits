from PySide6.QtWidgets import QFrame, QVBoxLayout


class Workspace(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("workspace")

        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)

        self.setLayout(layout)