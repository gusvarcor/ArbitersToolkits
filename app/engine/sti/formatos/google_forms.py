from app.engine.sti.jugador import Jugador
from app.engine.sti.nombre_parser import parsear_nombre

from app.engine.sti.nombre_formatos import AUTOMATICO


def importar_google_forms(
    ws,
    formato_nombre=AUTOMATICO
):
    """
    Importa un Excel generado por Google Forms.

    Formatos compatibles (por ahora):
    - NAYCC
    - Copa Revolución

    Se basa en los encabezados:
    - Nombre Completo
    - Fecha de nacimiento
    - FIDE ID
    - Federación
    """

    jugadores = []

    for fila in ws.iter_rows(min_row=2, values_only=True):

        if not any(fila):
            continue

        nombre = str(fila[1] or "").strip()

        datos = parsear_nombre(
            nombre,
            formato_nombre
        )
        print()
        print("===================================")
        print("FORMATO:", formato_nombre)
        print("ENTRADA :", nombre)
        print("SALIDA  :", datos.apellido_paterno, datos.apellido_materno, "|", datos.nombres)
        print("===================================")
        jugador = Jugador()

        jugador.apellido_paterno = datos.apellido_paterno
        jugador.apellido_materno = datos.apellido_materno
        jugador.nombres = datos.nombres

        # Fecha de nacimiento
        jugador.nacimiento = fila[2]

        # FIDE ID
        jugador.fide_id = fila[3]

        # Federación / País
        jugador.federacion = str(fila[4] or "").strip()
        jugador.pais = jugador.federacion

        jugadores.append(jugador)

    return jugadores