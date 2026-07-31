from PySide6.QtGui import QColor

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

from app.ui.sti.dialogs.candidate_selector_dialog import CandidateSelectorDialog


class PlayerTable(QWidget):

    def __init__(self):
        super().__init__()

        self.jugadores = []

        layout = QVBoxLayout(self)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "#",
            "Apellidos",
            "Nombres",
            "País",
            "Rating",
            "Confianza",
            "Estado",
        ])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table)

        # Doble clic sobre una fila
        self.table.cellDoubleClicked.connect(self.al_doble_clic)

    def poner_item(self, fila, columna, texto, color):
        item = QTableWidgetItem(str(texto))
        item.setBackground(color)
        self.table.setItem(fila, columna, item)

    def cargar_jugadores(self, jugadores):

        self.jugadores = jugadores

        self.table.setRowCount(len(jugadores))

        for fila, jugador in enumerate(jugadores):

            apellidos = jugador.apellido_paterno
            if getattr(jugador, "apellido_materno", ""):
                apellidos += " " + jugador.apellido_materno

            pais = getattr(jugador, "federacion", None) or jugador.pais
            rating = getattr(jugador, "elo_fide", None) or jugador.rating
            estado = getattr(jugador, "estado", "Pendiente")
            confianza = getattr(jugador, "confianza", 0)

            if estado == "ENCONTRADO":
                color = QColor(220, 255, 220)
            elif estado == "REVISAR":
                color = QColor(255, 250, 205)
            else:
                color = QColor(255, 220, 220)

            self.poner_item(fila, 0, fila + 1, color)
            self.poner_item(fila, 1, apellidos, color)
            self.poner_item(fila, 2, jugador.nombres, color)
            self.poner_item(fila, 3, pais, color)
            self.poner_item(fila, 4, rating, color)
            self.poner_item(fila, 5, f"{confianza}%", color)
            self.poner_item(fila, 6, estado, color)

    def al_doble_clic(self, fila, columna):

        jugador = self.jugadores[fila]

        dialogo = CandidateSelectorDialog(jugador, self)

        dialogo.exec()