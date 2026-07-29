from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.engine.sti.importador_excel import importar_excel


class ImportPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.jugadores = []

        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # ==========================================
        # Título
        # ==========================================

        titulo = QLabel("📥 Smart Tournament Import")
        titulo.setAlignment(Qt.AlignLeft)
        titulo.setObjectName("DashboardTitle")

        descripcion = QLabel(
            "Importa un archivo de Excel para comenzar el proceso "
            "de identificación de jugadores."
        )

        descripcion.setWordWrap(True)
        descripcion.setObjectName("DashboardDescription")

        # ==========================================
        # Botón
        # ==========================================

        self.btn_importar = QPushButton("Seleccionar archivo Excel")

        self.btn_importar.clicked.connect(self.importar_excel)

        # ==========================================
        # Información
        # ==========================================

        self.lbl_archivo = QLabel("Archivo: Ninguno")

        self.lbl_jugadores = QLabel("Jugadores importados: 0")

        # ==========================================
        # Layout
        # ==========================================

        layout.addWidget(titulo)
        layout.addWidget(descripcion)
        layout.addSpacing(10)
        layout.addWidget(self.btn_importar)
        layout.addSpacing(10)
        layout.addWidget(self.lbl_archivo)
        layout.addWidget(self.lbl_jugadores)
        layout.addStretch()

    def importar_excel(self):

        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo Excel",
            "",
            "Excel (*.xlsx *.xlsm)"
        )

        if not archivo:
            return

        self.lbl_archivo.setText(f"Archivo: {archivo}")

        try:

            self.jugadores = importar_excel(archivo)

            self.lbl_jugadores.setText(
                f"Jugadores importados: {len(self.jugadores)}"
            )

        except Exception as e:

            self.lbl_jugadores.setText(
                "Error al importar el archivo."
            )

            print(e)