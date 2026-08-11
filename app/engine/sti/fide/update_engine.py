"""
Update Engine del FIDE Data Engine.

Responsabilidad:

Coordinar toda la actualización de la base FIDE.
"""

from app.core.result import EngineResult

from app.engine.sti.fide.downloader import Downloader
from app.engine.sti.fide.schema_builder import SchemaBuilder
from app.engine.sti.fide.snapshot_manager import SnapshotManager
from app.engine.sti.fide.importer import Importer
from app.engine.sti.fide.metadata_manager import MetadataManager
from app.engine.sti.fide.integrity_checker import IntegrityChecker


class UpdateEngine:

    def __init__(self):

        self.downloader = Downloader()
        self.snapshot = SnapshotManager()
        self.schema = SchemaBuilder()
        self.importer = Importer()

    # ==========================================================

    def update(self):

        try:

            #
            # 1. Descargar
            #
            result = self.downloader.download_latest()

            if not result.success:
                return result

            #
            # 2. Leer metadata existente
            #
            metadata = MetadataManager()

            current_list = metadata.get("fide_list")

            metadata.close()

            #
            # 3. Crear snapshot
            #
            if current_list:

                try:

                    self.snapshot.create_snapshot(current_list)

                except FileExistsError:
                    pass

            #
            # 4. Reconstruir base
            #
            self.schema.rebuild_database()

            #
            # 5. Importar jugadores
            #
            imported = self.importer.import_players()

            #
            # 6. Escribir metadata
            #
            metadata = MetadataManager()

            metadata.set("imported_players", imported)

            if result.data is not None:
                metadata.set("fide_list", str(result.data))

            metadata.close()

            #
            # 7. Verificar integridad
            #
            checker = IntegrityChecker()

            ok, message = checker.check()

            checker.close()

            if not ok:
                return EngineResult.fail(message)

            return EngineResult.ok(
                message="Actualización completada correctamente.",
                data=imported
            )

        except Exception as ex:

            return EngineResult.fail(
                message=str(ex),
                error=ex
            )