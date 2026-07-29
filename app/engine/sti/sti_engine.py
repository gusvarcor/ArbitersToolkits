"""
sti_engine.py

Motor principal del Smart Tournament Import (STI).
"""

from app.engine.sti.importador_excel import importar_excel
from app.engine.sti.preparar_jugador import preparar_jugador


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

        return self.jugadores

    def preparar(self):
        """
        Prepara todos los jugadores importados.
        """

        for jugador in self.jugadores:
            preparar_jugador(jugador)

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