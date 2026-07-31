from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QRadioButton,
    QButtonGroup,
    QPushButton,
    QHBoxLayout,
)

from app.engine.sti.nombre_formatos import (
    NOMBRES_APELLIDOS,
    APELLIDOS_NOMBRES,
    APELLIDOS_COMA_NOMBRES,
    AUTOMATICO,
)


class ImportWizardDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Smart Import Wizard")
        self.resize(500, 350)

        layout = QVBoxLayout(self)

        titulo = QLabel("<h2>Formato de nombres</h2>")
        layout.addWidget(titulo)

        descripcion = QLabel(
            "Seleccione cómo vienen escritos los nombres "
            "en el archivo de Excel."
        )

        descripcion.setWordWrap(True)

        layout.addWidget(descripcion)

        self.group = QButtonGroup(self)

        self.rb1 = QRadioButton(
            "Apellidos Nombres\n"
            "PEREZ LOPEZ JUAN CARLOS"
        )

        self.rb2 = QRadioButton(
            "Nombres Apellidos\n"
            "JUAN CARLOS PEREZ LOPEZ"
        )

        self.rb3 = QRadioButton(
            "Apellidos, Nombres\n"
            "PEREZ LOPEZ, JUAN CARLOS"
        )

        self.rb4 = QRadioButton(
            "Detectar automáticamente"
        )

        self.group.addButton(self.rb1)
        self.group.addButton(self.rb2)
        self.group.addButton(self.rb3)
        self.group.addButton(self.rb4)

        self.rb4.setChecked(True)

        layout.addWidget(self.rb1)
        layout.addWidget(self.rb2)
        layout.addWidget(self.rb3)
        layout.addWidget(self.rb4)

        botones = QHBoxLayout()

        botones.addStretch()

        btn_cancelar = QPushButton("Cancelar")
        btn_aceptar = QPushButton("Aceptar")

        btn_cancelar.clicked.connect(self.reject)
        btn_aceptar.clicked.connect(self.accept)

        botones.addWidget(btn_cancelar)
        botones.addWidget(btn_aceptar)

        layout.addLayout(botones)

    def formato_seleccionado(self):

        if self.rb1.isChecked():
            return APELLIDOS_NOMBRES

        if self.rb2.isChecked():
            return NOMBRES_APELLIDOS

        if self.rb3.isChecked():
            return APELLIDOS_COMA_NOMBRES

        return AUTOMATICO