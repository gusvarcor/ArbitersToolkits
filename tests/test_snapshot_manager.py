"""
Prueba del SnapshotManager.
"""

from app.engine.sti.fide.snapshot_manager import SnapshotManager


def main():

    print("=" * 70)
    print("SNAPSHOT MANAGER TEST")
    print("=" * 70)
    print()

    manager = SnapshotManager()

    try:

        snapshot = manager.create_snapshot("2026-08")

        print("Snapshot creado correctamente.")
        print(snapshot)

    except FileExistsError:

        print("El snapshot ya existe.")

    print()

    print("=" * 70)
    print("SNAPSHOTS DISPONIBLES")
    print("=" * 70)
    print()

    for file in manager.list_snapshots():

        print(file.name)

    print()
    print("Prueba finalizada correctamente.")


if __name__ == "__main__":
    main()