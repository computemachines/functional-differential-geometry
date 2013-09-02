"""
see ``simplification.rst`` for an explanation.
"""

import numbers

from symbolic import *


def simplify(expr):
    if isinstance(expr, numbers.Number):
        return expr
    elif isinstance(expr, Num):
        return expr
    elif isinstance(expr, Sym):
        return expr
    elif isinstance(expr, Add):
        arg1 = simplify(expr.arg1)
        arg2 = simplify(expr.arg2)
        if arg2 == 0:
            return arg1
        elif arg1 == 0:
            return arg2
        else:
            return arg1 + arg2
    elif isinstance(expr, Mul):
        arg1 = simplify(expr.arg1)
        arg2 = simplify(expr.arg2)
        if arg2 == 0:
            return 0
        elif arg1 == 0:
            return 0
        elif arg2 == 1:
            return arg1
        elif arg1 == 1:
            return arg2
        else:
            return arg1 * arg2
    else:
        raise TypeError("can't handle {}".format(type(expr)))