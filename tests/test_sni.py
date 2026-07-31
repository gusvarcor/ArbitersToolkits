"""
test_sni.py

Pruebas del Smart Name Intelligence.
"""

from app.engine.sti.sni.smart_name_engine import SmartNameEngine


def main():

    sni = SmartNameEngine()

    pruebas = [

        "Lopez Hincapie Andres Felipe",

        "VAZQUEZ JUAREZ JUAN CARLOS",

        "Oscar Uriel Nuñez Duarte",

        "Luis Efrén Chávez Ramírez",

        "Juan Carlos Perez Lopez",

    ]

    for nombre in pruebas:

        sni.analizar(nombre)


if __name__ == "__main__":

    main()