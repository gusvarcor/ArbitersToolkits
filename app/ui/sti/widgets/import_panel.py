from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.engine.sti.sti_engine import STIEngine

from app.ui.sti.dialogs.import_wizard_dialog import (
    ImportWizardDialog,
)


class ImportPanel(QWidget):

    jugadores_importados = Signal(list)

    def __init__(self):
        super().__init__()

        # Motor del STI
        self.engine = STIEngine()

        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        titulo = QLabel("📥 Smart Tournament Import")
        titulo.setObjectName("DashboardTitle")

        descripcion = QLabel(
            "Importa un archivo de Excel para comenzar "
            "el proceso de identificación de jugadores."
        )

        descripcion.setWordWrap(True)
        descripcion.setObjectName("DashboardDescription")

        self.btn_importar = QPushButton(
            "Seleccionar archivo Excel"
        )

        self.btn_importar.clicked.connect(
            self.importar_excel
        )

        self.lbl_archivo = QLabel("Archivo: Ninguno")
        self.lbl_jugadores = QLabel("Jugadores importados: 0")

        layout.addWidget(titulo)
        layout.addWidget(descripcion)
        layout.addWidget(self.btn_importar)
        layout.addWidget(self.lbl_archivo)
        layout.addWidget(self.lbl_jugadores)

    def importar_excel(self):

        # ==========================================
        # SMART IMPORT WIZARD
        # ==========================================

        wizard = ImportWizardDialog(self)

        if not wizard.exec():
            return

        formato = wizard.formato_seleccionado()

        print()
        print("=" * 60)
        print("SMART IMPORT WIZARD")
        print("=" * 60)
        print(f"Formato seleccionado: {formato}")
        print("=" * 60)

        # ==========================================
        # Seleccionar archivo
        # ==========================================

        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo Excel",
            "",
            "Excel (*.xlsx *.xlsm)"
        )

        if not archivo:
            return

        self.lbl_archivo.setText(
            f"Archivo: {archivo}"
        )

        try:

            jugadores = self.engine.importar(
                archivo,
                formato
            )

            self.lbl_jugadores.setText(
                f"Jugadores importados: "
                f"{self.engine.total_jugadores()}"
            )

            self.jugadores_importados.emit(jugadores)

        except Exception as e:

            self.lbl_jugadores.setText(
                "Error al importar."
            )

            print(e)