
from pathlib import Path
from config import LFORTRAN_PATH
import sympy as sp
from parsing_fortran.asr import *


def main():
    fortran_file = Path("fortran_samples/02_expression.f90")
    print(fortran_file.read_text())
    asr = get_asr(fortran_file, LFORTRAN_PATH)
    cons, vars, ops = extract_from_asr(asr)
    print(f"Constants: {cons}")
    print(f"Variables: {vars}")
    print(f"Operators: {ops}")
    expr = build_sympy_expr(cons, vars)
    if expr:
        x = sp.Symbol('x', real=True)
        print(f"\nSymPy expression: {expr}")
        print(f"Derivative: {sp.diff(expr, x)}")
        print(f"At x=5: {expr.subs(x, 5)}")
    else:
        print("\nCould not build expression")


if __name__ == '__main__':
    main()