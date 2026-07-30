"""
sti_engine.py

Motor principal del Smart Tournament Import (STI).
"""

from app.engine.sti.importador_excel import importar_excel
from app.engine.sti.preparar_jugador import preparar_jugador
from app.engine.sti.fide import buscar_por_apellidos
from app.engine.sti.comparador import comparar


class STIEngine:

    def __init__(self):
        self.jugadores = []

    def importar(self, archivo):
        """
        Importa un archivo Excel y prepara automáticamente
        todos los jugadores para la búsqueda FIDE.
        """

        self.jugadores = importar_excel(archivo)

        self.preparar()

        # Sprint 9:
        # Buscar únicamente el primer jugador
        self.buscar_primer_jugador()

        return self.jugadores

    def preparar(self):
        """
        Prepara todos los jugadores importados.
        """

        for jugador in self.jugadores:
            preparar_jugador(jugador)

    def buscar_primer_jugador(self):
        """
        Busca en FIDE únicamente al primer jugador
        para validar todo el flujo.
        """

        if not self.jugadores:
            return

        jugador = self.jugadores[0]

        nombre_busqueda = (
            f"{jugador.apellido_paterno} "
            f"{jugador.apellido_materno}, "
            f"{jugador.nombres}"
        ).strip()

        print()
        print("=" * 60)
        print("BÚSQUEDA FIDE")
        print("=" * 60)
        print(f"Jugador: {nombre_busqueda}")

        candidatos = buscar_por_apellidos(
            jugador.apellido_paterno,
            jugador.apellido_materno
        )

        print(f"Candidatos encontrados: {len(candidatos)}")

        if not candidatos:
            print("No se encontraron candidatos.")
            print("=" * 60)
            return

        resultado = comparar(jugador, candidatos)

        print()

        if resultado["encontrado"]:

            fideid, nombre, pais, elo = resultado["mejor"]

            print("Mejor candidato")
            print("---------------------------")
            print(f"Nombre     : {nombre}")
            print(f"FIDE ID    : {fideid}")
            print(f"Federación : {pais}")
            print(f"ELO        : {elo}")
            print(f"Confianza  : {resultado['confianza']}%")

        else:

            print("No hubo coincidencias.")

        print("=" * 60)

    def obtener_jugadores(self):
        """
        Devuelve la lista actual de jugadores.
        """

        return self.jugadores

    def total_jugadores(self):
        """
        Devuelve el número de jugadores cargados.
        """

        return len(self.jugadores)

    def limpiar(self):
        """
        Limpia la sesión actual.
        """

        self.jugadores.clear()