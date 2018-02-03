from symbolic import *
import operator

x = Sym("x")
f = Sym("f")

def test_equality():
    assert f == f
    assert x == x
    assert f(x) == f(x)

def test_subs():
    assert x.subs(x=1) == 1
    assert f(x).subs(x=1) == f(1)

def test_expr_building():
    assert f(x).__repr__() == "f(x)"
