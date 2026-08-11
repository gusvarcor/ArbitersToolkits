"""
Runner de pruebas rápidas.

No ejecuta pruebas de integración.
"""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).parent

TESTS = [
    "test_downloader.py",
    "test_importer.py",
    "test_metadata_manager.py",
    "test_schema_builder.py",
    "test_schema_rebuild.py",
    "test_snapshot_manager.py",
    "test_integrity_checker.py",
    "test_sni.py",
]


def run(test_name):

    module = f"tests.{Path(test_name).stem}"

    print("=" * 70)
    print(module)
    print("=" * 70)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            module
        ],
        cwd=ROOT
    )

    print()

    return result.returncode


def main():

    failures = 0

    for test in TESTS:

        failures += run(test)

    print("=" * 70)

    if failures == 0:

        print("✅ TODOS LOS TESTS RÁPIDOS PASARON")

    else:

        print(f"❌ {failures} TEST(S) FALLARON")

    print("=" * 70)


if __name__ == "__main__":
    main()