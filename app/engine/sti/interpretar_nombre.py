# ==========================================
# ArbiterTools
# Interpretación de nombres
# ==========================================

from limpiar import limpiar_nombre


def interpretar_nombre(
    nombre_completo=None,
    nombres=None,
    apellidos=None,
    apellido_paterno=None,
    apellido_materno=None,
):
    """
    Convierte cualquier combinación de datos de entrada
    a una estructura estándar utilizada por ArbiterTools.

    Devuelve un diccionario.
    """

    datos = {
        "nombre_completo": limpiar_nombre(nombre_completo) if nombre_completo else "",
        "nombres": limpiar_nombre(nombres) if nombres else "",
        "apellidos": limpiar_nombre(apellidos) if apellidos else "",
        "apellido_paterno": limpiar_nombre(apellido_paterno) if apellido_paterno else "",
        "apellido_materno": limpiar_nombre(apellido_materno) if apellido_materno else "",
    }

    return datos