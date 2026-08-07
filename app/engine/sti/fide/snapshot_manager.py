"""
Snapshot Manager del FIDE Data Engine.

Responsabilidad:

- Crear snapshots de fide.db.
- Listar snapshots.
- Restaurar snapshots.

No conoce MetadataManager.
No conoce UpdateEngine.
"""

import shutil
from pathlib import Path

from app.core.config import AppConfig


class SnapshotManager:

    def __init__(self):

        self.database = AppConfig.FIDE_DB

        self.archive = AppConfig.SQLITE_DIR / "archive"

        self.archive.mkdir(parents=True, exist_ok=True)

    # ==========================================================

    def create_snapshot(self, fide_list):

        """
        Crea un snapshot de la base de datos utilizando
        la versión de la lista FIDE recibida.
        """

        if not self.database.exists():

            raise FileNotFoundError(
                f"No existe la base de datos:\n{self.database}"
            )

        destination = self.archive / f"fide_{fide_list}.db"

        if destination.exists():

            raise FileExistsError(
                f"Ya existe el snapshot:\n{destination}"
            )

        shutil.copy2(self.database, destination)

        return destination

    # ==========================================================

    def list_snapshots(self):

        """
        Devuelve todos los snapshots disponibles.
        """

        return sorted(
            self.archive.glob("*.db"),
            reverse=True
        )

    # ==========================================================

    def restore_snapshot(self, snapshot_file):

        """
        Restaura un snapshot.
        """

        snapshot = Path(snapshot_file)

        if not snapshot.exists():

            raise FileNotFoundError(snapshot)

        shutil.copy2(snapshot, self.database)

        return self.database