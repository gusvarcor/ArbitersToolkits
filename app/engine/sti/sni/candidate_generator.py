"""
candidate_generator.py

Genera distintas interpretaciones posibles
de un nombre completo.
"""

from dataclasses import dataclass

from app.engine.sti.nombre_formatos import (
    NOMBRES_APELLIDOS,
    APELLIDOS_NOMBRES,
)


@dataclass
class NameCandidate:

    formato: str

    apellido_paterno: str

    apellido_materno: str

    nombres: str


def generar_candidatos(nombre_completo: str):

    partes = nombre_completo.strip().split()

    candidatos = []

    if len(partes) < 2:
        return candidatos

    # ---------------------------------------
    # Interpretación:
    # NOMBRES -> APELLIDOS
    # ---------------------------------------

    if len(partes) == 2:

        candidatos.append(

            NameCandidate(

                formato=NOMBRES_APELLIDOS,

                apellido_paterno=partes[1],

                apellido_materno="",

                nombres=partes[0],

            )

        )

    else:

        candidatos.append(

            NameCandidate(

                formato=NOMBRES_APELLIDOS,

                apellido_paterno=partes[-2],

                apellido_materno=partes[-1],

                nombres=" ".join(partes[:-2]),

            )

        )

    # ---------------------------------------
    # Interpretación:
    # APELLIDOS -> NOMBRES
    # ---------------------------------------

    if len(partes) == 2:

        candidatos.append(

            NameCandidate(

                formato=APELLIDOS_NOMBRES,

                apellido_paterno=partes[0],

                apellido_materno="",

                nombres=partes[1],

            )

        )

    else:

        candidatos.append(

            NameCandidate(

                formato=APELLIDOS_NOMBRES,

                apellido_paterno=partes[0],

                apellido_materno=partes[1],

                nombres=" ".join(partes[2:]),

            )

        )

    return candidatos