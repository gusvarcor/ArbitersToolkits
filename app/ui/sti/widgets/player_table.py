from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)


class PlayerTable(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "#",
            "Apellidos",
            "Nombres",
            "País",
            "Rating",
            "Estado",
        ])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table)

    def cargar_jugadores(self, jugadores):

        self.table.setRowCount(len(jugadores))

        for fila, jugador in enumerate(jugadores):

            print(vars(jugador))
            apellidos = jugador.apellido_paterno

            if getattr(jugador, "apellido_materno", ""):
                apellidos += " " + jugador.apellido_materno

            self.table.setItem(
                fila,
                0,
                QTableWidgetItem(str(fila + 1))
            )

            self.table.setItem(
                fila,
                1,
                QTableWidgetItem(apellidos)
            )

            self.table.setItem(
                fila,
                2,
                QTableWidgetItem(jugador.nombres)
            )

            self.table.setItem(
                fila,
                3,
                QTableWidgetItem(str(jugador.pais))
            )

            self.table.setItem(
                fila,
                4,
                QTableWidgetItem(str(jugador.rating))
            )

            self.table.setItem(
                fila,
                5,
                QTableWidgetItem("Pendiente")
            )