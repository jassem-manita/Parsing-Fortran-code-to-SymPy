import pytest
import sympy as sp
from parsing_fortran import asr
import json


def test_extract_from_asr_basic():
    
    with open("tests/full_asr.json") as f:
        asr_json = json.load(f)
    body = asr_json["fields"]["symtab"]["fields"]["test"]["fields"]["body"]
    assignment = body[0]["fields"]["value"]
    cons, variables, ops = asr.extract_from_asr(assignment)
    assert cons == [2.0, 3.0]
    assert 'x' in variables
    assert 'Mul' in ops and 'Add' in ops



def test_build_sympy_expr():
    cons = [2.0, 3.0]
    variables = ['x', 'y']
    expr = asr.build_sympy_expr(cons, variables)
    x = sp.Symbol('x', real=True)
    assert expr == 2.0 * x + 3.0



def test_build_sympy_expr_fail():
    cons = [2.0]
    variables = ['y']
    expr = asr.build_sympy_expr(cons, variables)
    assert expr is None
