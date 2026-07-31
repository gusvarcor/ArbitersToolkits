"""
nombre_formatos.py

Define los formatos de nombres soportados por el
Smart Tournament Import.
"""

# Formatos soportados

NOMBRES_APELLIDOS = "NOMBRES_APELLIDOS"

APELLIDOS_NOMBRES = "APELLIDOS_NOMBRES"

APELLIDOS_COMA_NOMBRES = "APELLIDOS_COMA_NOMBRES"

AUTOMATICO = "AUTOMATICO"


FORMATO_DESCRIPCIONES = {

    NOMBRES_APELLIDOS:
        "Juan Carlos Perez Lopez",

    APELLIDOS_NOMBRES:
        "Perez Lopez Juan Carlos",

    APELLIDOS_COMA_NOMBRES:
        "Perez Lopez, Juan Carlos",

    AUTOMATICO:
        "Detección automática"
}