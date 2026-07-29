# ==========================================
# ArbiterTools
# Generador XML para Swiss-Manager
# ==========================================

from xml.etree.ElementTree import Element, SubElement, ElementTree
from xml.dom import minidom
from datetime import datetime
import io


def texto(valor):
    """Convierte None en cadena vacía."""
    if valor is None:
        return ""
    return str(valor)


def fecha_xml(fecha):
    """
    Convierte una fecha al formato AAAAMMDD.
    """

    if not fecha:
        return ""

    if isinstance(fecha, datetime):
        return fecha.strftime("%Y%m%d")

    try:
        return fecha.strftime("%Y%m%d")
    except Exception:
        pass

    try:
        cadena = str(fecha)

        if "-" in cadena:
            return cadena.replace("-", "")[:8]

        if "/" in cadena:
            partes = cadena.split("/")

            if len(partes) == 3:
                dia, mes, anio = partes
                return f"{anio}{mes.zfill(2)}{dia.zfill(2)}"

        return cadena[:8]

    except Exception:
        return ""


def generar_xml(jugadores, archivo_salida):

    raiz = Element("Players")

    consecutivo = 1

    for jugador in jugadores:

        player = SubElement(raiz, "Player")

        # =====================================
        # APELLIDOS
        # =====================================

        apellidos = texto(jugador.apellido_paterno)

        if getattr(jugador, "apellido_materno", ""):
            apellidos += " " + texto(jugador.apellido_materno)

        # =====================================
        # CAMPOS OBLIGATORIOS
        # =====================================

        player.set("PlayerUniqueId", str(consecutivo))
        player.set("Lastname", apellidos)
        player.set("Firstname", texto(jugador.nombres))

        # =====================================
        # CAMPOS OPCIONALES
        # =====================================

        if getattr(jugador, "pais", ""):
            player.set("Federation", texto(jugador.pais))

        if getattr(jugador, "grupo", ""):
            player.set("Group", texto(jugador.grupo))

        if getattr(jugador, "elo", None):
            player.set("Rating", texto(jugador.elo))

        if getattr(jugador, "nacimiento", None):
            player.set(
                "Birthday",
                fecha_xml(jugador.nacimiento)
            )

        if getattr(jugador, "titulo", ""):
            player.set("Title", texto(jugador.titulo))

        if getattr(jugador, "fideid", None):
            player.set("FIDEId", texto(jugador.fideid))

        consecutivo += 1

    xml_bytes = ElementTree(raiz)

    buffer = io.BytesIO()

    xml_bytes.write(
        buffer,
        encoding="utf-8",
        xml_declaration=True
    )

    xml = minidom.parseString(buffer.getvalue())

    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        archivo.write(
            xml.toprettyxml(indent="    ")
        )

    print()
    print("=" * 60)
    print("XML generado correctamente")
    print(archivo_salida)
    print("=" * 60)