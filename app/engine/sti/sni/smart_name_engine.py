"""
smart_name_engine.py

Motor Smart Name Intelligence (SNI).
"""

from app.engine.sti.sni.candidate_generator import (
    generar_candidatos,
)

from app.engine.sti.sni.scorer import (
    CandidateScorer,
)


class SmartNameEngine:

    def __init__(self):

        self.scorer = CandidateScorer()

    def analizar(self, nombre_completo):

        candidatos = generar_candidatos(nombre_completo)

        print()
        print("=" * 60)
        print("SMART NAME INTELLIGENCE")
        print("=" * 60)
        print("Entrada:")
        print(nombre_completo)
        print()

        mejor = None
        mejor_score = -1

        for i, candidato in enumerate(candidatos, start=1):

            score = self.scorer.score(candidato)

            print(f"Opción {i}")
            print(f"Formato : {candidato.formato}")
            print(
                f"Apellidos: "
                f"{candidato.apellido_paterno} "
                f"{candidato.apellido_materno}"
            )
            print(f"Nombres : {candidato.nombres}")
            print(f"Score   : {score}")
            print("-" * 40)

            if score > mejor_score:

                mejor = candidato
                mejor_score = score

        print()

        print("MEJOR OPCIÓN")
        print(f"Formato : {mejor.formato}")
        print(
            f"Apellidos: "
            f"{mejor.apellido_paterno} "
            f"{mejor.apellido_materno}"
        )
        print(f"Nombres : {mejor.nombres}")
        print(f"Score   : {mejor_score}")

        return mejor