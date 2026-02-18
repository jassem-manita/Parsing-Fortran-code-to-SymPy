import pytest
import sympy as sp
from parsing_fortran import asr


def test_extract_from_asr_basic():
    asr_str = '''
    (RealConstant)
        2.0
    (Var 1 x)
    Mul
    (RealConstant)
        3.0
    Add
    '''
    cons, vars, ops = asr.extract_from_asr(asr_str)
    assert cons == [2.0, 3.0]
    assert 'x' in vars
    assert 'Mul' in ops and 'Add' in ops


def test_build_sympy_expr():
    cons = [2.0, 3.0]
    vars_ = ['x', 'y']
    expr = asr.build_sympy_expr(cons, vars_)
    x = sp.Symbol('x', real=True)
    assert expr == 2.0 * x + 3.0


def test_build_sympy_expr_fail():
    cons = [2.0]
    vars_ = ['y']
    expr = asr.build_sympy_expr(cons, vars_)
    assert expr is None
