import subprocess
import re
from pathlib import Path
import sympy as sp


def get_asr(fortran_file, lfortran_path):
    """
    Run LFortran to get the ASR

    Parameters
    ==========
    fortran_file : str
        Path to the Fortran source file
    lfortran_path : str
        Path to the LFortran executable

    Returns
    =======
    str
        The ASR output as a string with ANSI color codes stripped
    """
    result = subprocess.run([lfortran_path, '--show-asr', str(fortran_file)], capture_output=True, text=True)
    return re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)


def extract_from_asr(asr):
    """
    Extract from ASR

    Parameters
    ==========
    asr : str
        ASR output as a string

    Returns
    =======
    tuple
        (constants, variables, operators)
    """
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
    """
    Build SymPy expression from extracted constants and variables
    Currently hardcoded for the pattern c1 * x + c2

    Parameters
    ==========
    cons : list
        List of constants
    vars : list
        List of variable names

    Returns
    =======
    sympy.Expr or None
    """
    if 'x' not in vars or len(cons) < 2:
        return None
    x = sp.Symbol('x', real=True)
    return cons[0] * x + cons[1]
