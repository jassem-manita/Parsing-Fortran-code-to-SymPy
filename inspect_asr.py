
import subprocess
import json
import sys
from pathlib import Path
from config import LFORTRAN_PATH

def pretty_print_json(obj, indent=0):
    spacing = '  ' * indent
    if isinstance(obj, dict):
        for k, v in obj.items():
            print(f"{spacing}{k}:")
            pretty_print_json(v, indent + 1)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            print(f"{spacing}- [{i}]")
            pretty_print_json(item, indent + 1)
    else:
        print(f"{spacing}{obj}")



if len(sys.argv) < 2:
    sys.exit(1)
fortran_file = Path(sys.argv[1])

print(f"File: {fortran_file.name}")
print(fortran_file.read_text())

result = subprocess.run(
    [LFORTRAN_PATH, '--show-asr', '--json', str(fortran_file)],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print("LFortran error:")
    print(result.stderr)
    sys.exit(1)

print("\nASR (JSON tree):")
asr_json = json.loads(result.stdout)
pretty_print_json(asr_json)