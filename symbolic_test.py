
from symbolic import *
import operator

x = Sym("x")
y = Sym("y")
f = Sym("f")
g = Sym("g")

def test_equality():
    assert f == f
    assert x == x
    assert f(x) == f(x)
    assert f(1) == f(1)

def test_subs():
    assert x.subs(x=1) == 1
    assert f(x).subs(x=1) == f(1)
    assert f(x, y).subs(f=g, x=y, y=x) == g(y, x)

def test_expr_building():
    assert f(x).__repr__() == "f(x)"

# def test_currying():
#     assert f(x, x) == f(x)(x)

f(x, 1)(2)
