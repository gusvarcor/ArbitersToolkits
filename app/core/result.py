"""
Resultado estándar utilizado por todos los motores de ArbitersToolkits.

Evita lanzar excepciones hacia la interfaz gráfica y permite que cada
módulo informe correctamente si la operación fue exitosa.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class EngineResult:
    """
    Resultado estándar de cualquier operación del motor.
    """

    success: bool

    message: str = ""

    data: Any = None

    file_path: Path | None = None

    error: Exception | None = None

    @classmethod
    def ok(
        cls,
        message: str = "",
        data: Any = None,
        file_path: Path | None = None,
    ):
        return cls(
            success=True,
            message=message,
            data=data,
            file_path=file_path,
        )

    @classmethod
    def fail(
        cls,
        message: str,
        error: Exception | None = None,
    ):
        return cls(
            success=False,
            message=message,
            error=error,
        )