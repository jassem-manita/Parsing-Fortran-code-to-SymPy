import subprocess
import json
from pathlib import Path
import sympy as sp


def get_asr(fortran_file, lfortran_path):
    """
    Run LFortran to get the ASR in JSON format

    Parameters
    ==========
    fortran_file : str
        Path to the Fortran source file
    lfortran_path : str
        Path to the LFortran executable

    Returns
    =======
    dict
        The ASR output parsed as a JSON dictionary
    """
    result = subprocess.run([lfortran_path, '--show-asr', '--json', str(fortran_file)], capture_output=True, text=True)
    return json.loads(result.stdout)



def extract_from_asr(asr):
    """
    Extract from ASR

    Parameters
    ==========
    asr : dict
        ASR output as a JSON dictionary

    Returns
    =======
    tuple
        (constants, variables, operators)
    """
    cons = []
    vars_ = []
    ops = []

    def walk(node):
        if isinstance(node, dict):
            node_type = node.get('node')
            fields = node.get('fields', {})
            if node_type == 'RealConstant':
                value = fields.get('r')
                if value is not None:
                    try:
                        cons.append(float(value))
                    except Exception:
                        pass
            elif node_type == 'Var':
                v = fields.get('v')
                if isinstance(v, str):
                    vars_.append(v.split(' (')[0])
            elif node_type in {'RealBinOp', 'IntegerBinOp'}:
                op = fields.get('op')
                if op in {'Add', 'Sub', 'Mul', 'Div'}:
                    ops.append(op)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(asr)
    return cons, vars_, ops


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
