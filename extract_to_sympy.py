

import sys
from pathlib import Path
from config import LFORTRAN_PATH
import sympy as sp
from parsing_fortran.asr import *



def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    fortran_file = Path(sys.argv[1])
    print(fortran_file.read_text())
    asr = get_asr(fortran_file, LFORTRAN_PATH)
    if not asr:
        print("Error: LFortran did not return any ASR output.")
        sys.exit(1)
    cons, variables, ops = extract_from_asr(asr)
    print(f"Constants: {cons}")
    print(f"Variables: {variables}")
    print(f"Operators: {ops}")
    expr = build_sympy_expr(cons, variables)
    if expr:
        x = sp.Symbol('x', real=True)
        print(f"\nSymPy expression: {expr}")
        print(f"Derivative: {sp.diff(expr, x)}")
        print(f"At x=5: {expr.subs(x, 5)}")
    else:
        print("\nCould not build expression")


if __name__ == '__main__':
    main()