import subprocess
from pathlib import Path
from config import LFORTRAN_PATH

fortran_file = Path("fortran_samples/01_simple.f90")

print(f"File: {fortran_file.name}")
print(fortran_file.read_text())

result = subprocess.run(
    [LFORTRAN_PATH, '--show-asr', str(fortran_file)],
    capture_output=True,
    text=True
)

print("\nASR:")
print(result.stdout)