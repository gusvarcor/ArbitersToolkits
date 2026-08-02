"""
Prueba del Downloader del FIDE Data Engine.
"""

from app.engine.sti.fide.downloader import Downloader


def main():

    print("=" * 60)
    print("FIDE DATA ENGINE")
    print("=" * 60)
    print()

    downloader = Downloader()

    resultado = downloader.download_latest()

    if resultado.success:

        print("✅ Descarga completada correctamente.")
        print()
        print("Archivo XML:")
        print(resultado.file_path)

    else:

        print("❌ Error")
        print()
        print(resultado.message)


if __name__ == "__main__":
    main()