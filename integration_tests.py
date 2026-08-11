"""
Pruebas de integración.

Aquí van las pruebas que tardan varios minutos.
"""

import subprocess
import sys

TESTS = [
    "tests.test_update_engine",
]


def main():

    for test in TESTS:

        print("=" * 70)
        print(test)
        print("=" * 70)

        subprocess.run(
            [
                sys.executable,
                "-m",
                test
            ]
        )


if __name__ == "__main__":
    main()