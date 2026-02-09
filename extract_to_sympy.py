import subprocess
import re
from pathlib import Path
from config import LFORTRAN_PATH
import sympy as sp


def get_asr(fortran_file):
    result = subprocess.run(
        [LFORTRAN_PATH, '--show-asr', str(fortran_file)],
        capture_output=True,
        text=True
    )
    return re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)


def extract_from_asr(asr):
    lines = asr.split('\n')
    cons = []
    vars = []
    ops = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        if 'RealConstant' in line and i + 1 < len(lines):
            match = re.search(r'(\d+\.\d+)', lines[i + 1].strip())
            if match:
                cons.append(float(match.group(1)))
        
        match = re.match(r'\(Var\s+\d+\s+(\w+)\)', stripped)
        if match:
            vars.append(match.group(1))
        
        if stripped in ['Mul', 'Add', 'Sub', 'Div']:
            ops.append(stripped)
    
    return cons, vars, ops


def build_sympy_expr(cons, vars):
    #
    if 'x' not in vars or len(cons) < 2:
        return None
    
    x = sp.Symbol('x', real=True)
    # hardcoded for this exemple
    return cons[0] * x + cons[1]


if __name__ == '__main__':
    fortran_file = Path("fortran_samples/02_expression.f90")

    print(fortran_file.read_text())
    
    asr = get_asr(fortran_file)
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