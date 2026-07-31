from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout,
    QHeaderView,
)


class CandidateSelectorDialog(QDialog):

    def __init__(self, jugador, parent=None):
        super().__init__(parent)

        self.jugador = jugador

        self.setWindowTitle("Seleccionar jugador FIDE")
        self.resize(800, 500)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("<b>Jugador importado</b>"))

        nombre = (
            f"{jugador.apellido_paterno} "
            f"{jugador.apellido_materno} "
            f"{jugador.nombres}"
        ).strip()

        layout.addWidget(QLabel(nombre))

        layout.addSpacing(10)

        layout.addWidget(QLabel("<b>Posibles coincidencias</b>"))

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "FIDE ID",
            "Nombre",
            "Federación",
            "ELO",
        ])

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table)

        botones = QHBoxLayout()

        self.btn_seleccionar = QPushButton("Seleccionar")
        self.btn_cancelar = QPushButton("Cancelar")

        botones.addStretch()
        botones.addWidget(self.btn_seleccionar)
        botones.addWidget(self.btn_cancelar)

        layout.addLayout(botones)

        self.btn_cancelar.clicked.connect(self.reject)

        self.cargar_candidatos()

    def cargar_candidatos(self):

        candidatos = getattr(self.jugador, "candidatos", [])

        self.table.setRowCount(len(candidatos))

        for fila, candidato in enumerate(candidatos):

            fideid, nombre, federacion, elo = candidato

            self.table.setItem(fila, 0, QTableWidgetItem(str(fideid)))
            self.table.setItem(fila, 1, QTableWidgetItem(str(nombre)))
            self.table.setItem(fila, 2, QTableWidgetItem(str(federacion)))
            self.table.setItem(fila, 3, QTableWidgetItem(str(elo)))