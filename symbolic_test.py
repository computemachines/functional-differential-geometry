from symbolic import *

x = Sym("x")

def test_subs():
    assert x.subs(x=1) == 1
