"""
Update Engine del FIDE Data Engine.

Responsabilidad:

Coordinar la actualización completa de la base FIDE.

No implementa lógica de negocio.
Únicamente coordina los módulos existentes.
"""

from pathlib import Path

from app.core.config import AppConfig

from app.engine.sti.fide.downloader import Downloader
from app.engine.sti.fide.importer import Importer
from app.engine.sti.fide.metadata_manager import MetadataManager
from app.engine.sti.fide.snapshot_manager import SnapshotManager
from app.engine.sti.fide.integrity_checker import IntegrityChecker


class UpdateEngine:

    def __init__(self):

        self.downloader = Downloader()

        self.snapshot = SnapshotManager()

        self.importer = Importer()

        self.metadata = MetadataManager()

        self.checker = IntegrityChecker()

    # ==========================================================

    def update(self):

        print("=" * 70)
        print("FIDE UPDATE ENGINE")
        print("=" * 70)
        print()

        # ------------------------------------------------------
        # 1. Descargar
        # ------------------------------------------------------

        print("1. Descargando lista FIDE...")

        xml_file = self.downloader.download()

        print("OK")
        print()

        # ------------------------------------------------------
        # 2. Snapshot
        # ------------------------------------------------------

        if Path(AppConfig.FIDE_DB).exists():

            print("2. Creando snapshot...")

            try:

                snapshot = self.snapshot.create_snapshot()

                print(snapshot.name)

            except FileExistsError:

                print("Snapshot ya existente.")

            print()

        # ------------------------------------------------------
        # 3. Importar
        # ------------------------------------------------------

        print("3. Importando jugadores...")

        imported = self.importer.import_players()

        print(f"{imported} jugadores importados.")

        print()

        # ------------------------------------------------------
        # 4. Metadata
        # ------------------------------------------------------

        print("4. Actualizando metadata...")

        self.metadata.set(
            "imported_players",
            imported
        )

        print("OK")
        print()

        # ------------------------------------------------------
        # 5. Integridad
        # ------------------------------------------------------

        print("5. Verificando integridad...")

        ok, message = self.checker.check()

        if not ok:

            raise RuntimeError(message)

        print(message)

        print()

        print("=" * 70)
        print("ACTUALIZACIÓN FINALIZADA")
        print("=" * 70)

        return True

    # ==========================================================

    def close(self):

        self.metadata.close()

        self.checker.close()