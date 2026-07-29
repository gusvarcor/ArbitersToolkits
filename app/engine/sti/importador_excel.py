from openpyxl import load_workbook

from app.engine.sti.formatos.google_forms import importar_google_forms


def importar_excel(ruta_excel):
    """
    Importador principal del STI.

    Analiza los encabezados del Excel y selecciona
    automáticamente el importador adecuado.
    """

    wb = load_workbook(ruta_excel, data_only=True)
    ws = wb.active

    # Leer encabezados
    encabezados = [
        str(celda.value).strip() if celda.value else ""
        for celda in ws[1]
    ]

    # ==========================================
    # Google Forms
    # ==========================================

    if "Nombre Completo" in encabezados:
        return importar_google_forms(ws)

    # ==========================================
    # Formato desconocido
    # ==========================================

    raise ValueError(
        "Formato de Excel no reconocido.\n\n"
        "El STI todavía no tiene un importador para este tipo de archivo."
    )