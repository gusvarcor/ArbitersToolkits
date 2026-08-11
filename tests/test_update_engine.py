"""
Prueba de integración del Update Engine.
"""

from app.engine.sti.fide.update_engine import UpdateEngine


def main():

    print("=" * 70)
    print("UPDATE ENGINE TEST")
    print("=" * 70)
    print()

    engine = UpdateEngine()

    result = engine.update()

    print()
    print("RESULTADO")
    print("-" * 70)

    if result.success:

        print("✅ Actualización completada correctamente.")
        print(f"Jugadores procesados: {result.data}")

    else:

        print("❌ Actualización fallida.")
        print(result.message)

        if result.error:

            print()
            print(type(result.error).__name__)
            print(result.error)

    print()
    print("=" * 70)
    print("FIN DE LA PRUEBA")
    print("=" * 70)


if __name__ == "__main__":

    main()