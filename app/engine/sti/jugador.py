from dataclasses import dataclass
from datetime import date


@dataclass
class Jugador:
    id: int = 0
    grupo: str = ""

    apellido_paterno: str = ""
    apellido_materno: str = ""
    nombres: str = ""

    rating: int = 0

    nacimiento: date | None = None

    genero: str = ""

    pais: str = ""

    fide_id: int | None = None

    titulo: str = ""

    federacion: str = ""

    elo_fide: int | None = None

    id_nacional: str = ""

    encontrado: bool = False

    confianza: int = 0
        # Datos generados por ArbiterTools

    clave_busqueda: str = ""

    candidatos: list | None = None

    estado: str = "PENDIENTE"

    observaciones: str = ""