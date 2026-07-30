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
        self.jugadores = importar_excel(archivo)
        self.preparar()

        # Sprint 10:
        # Procesar todos los jugadores
        self.buscar_todos()

        return self.jugadores

    def preparar(self):
        for jugador in self.jugadores:
            preparar_jugador(jugador)

    def buscar_jugador(self, jugador):

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

        jugador.candidatos = candidatos

        print(f"Candidatos encontrados: {len(candidatos)}")

        if not candidatos:
            jugador.encontrado = False
            jugador.estado = "PENDIENTE"
            print("No se encontraron candidatos.")
            print("=" * 60)
            return

        resultado = comparar(jugador, candidatos)

        if resultado["encontrado"]:
            fideid, nombre, pais, elo = resultado["mejor"]

            jugador.fide_id = fideid
            jugador.federacion = pais
            jugador.elo_fide = elo
            jugador.confianza = resultado["confianza"]
            jugador.encontrado = True
            jugador.estado = "ENCONTRADO"

            print("\nMejor candidato")
            print("---------------------------")
            print(f"Nombre     : {nombre}")
            print(f"FIDE ID    : {fideid}")
            print(f"Federación : {pais}")
            print(f"ELO        : {elo}")
            print(f"Confianza  : {resultado['confianza']}%")
        else:
            jugador.encontrado = False
            jugador.estado = "PENDIENTE"
            print("\nNo hubo coincidencias.")

        print("=" * 60)

    def buscar_primer_jugador(self):
        if self.jugadores:
            self.buscar_jugador(self.jugadores[0])

    def buscar_todos(self):
        for jugador in self.jugadores:
            self.buscar_jugador(jugador)

    def obtener_jugadores(self):
        return self.jugadores

    def total_jugadores(self):
        return len(self.jugadores)

    def limpiar(self):
        self.jugadores.clear()
