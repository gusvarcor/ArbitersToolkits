"""
dictionary_builder.py

Constructor del diccionario maestro utilizado
por Smart Name Intelligence.
"""

from collections import defaultdict


class DictionaryBuilder:

    def __init__(self):

        self.palabras = defaultdict(

            lambda: {

                "nombre": 0,

                "apellido": 0,

            }

        )

    def agregar_nombre(self, palabra):

        palabra = palabra.lower().strip()

        if not palabra:

            return

        self.palabras[palabra]["nombre"] += 1

    def agregar_apellido(self, palabra):

        palabra = palabra.lower().strip()

        if not palabra:

            return

        self.palabras[palabra]["apellido"] += 1

    def obtener_diccionario(self):

        return dict(self.palabras)