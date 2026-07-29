from Librerias.limpiar import crear_clave


def preparar_jugador(jugador):
    """
    Prepara un jugador para ser buscado
    en la base FIDE.
    """

    nombre_completo = (
        f"{jugador.apellido_paterno} "
        f"{jugador.apellido_materno} "
        f"{jugador.nombres}"
    )

    jugador.clave_busqueda = crear_clave(nombre_completo)

    return jugador