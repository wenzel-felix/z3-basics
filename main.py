from z3 import *

elems = [-7, -3, -2, -3, 9000, 5, 8]


def zerosum(xs):
    n = len(xs)

    ss = [Bool(f"ss[{i}]") for i in range(n)]

    s = Optimize()

    s.add(Sum([If(ss[i], xs[1], 0) for i in range(n)]) == 0)
    length = Sum([If(ss[i], 1, 0) for i in range(n)])

    s.maximize(length)

    if s.check() == sat:
        m = s.model()
        print([xs[i] for i in range(n) if m.eval(ss[i]) is True])
    else:
        print("No solution")


zerosum(elems)


def kn(ws, vs, M):
    n = len(ws)

    ns = [Int(f"ns[{i}]") for i in range(n)]
    s = Optimize()

    s.add(And([ns[i] >= 0 for i in range(n)]))
    s.add(Sum([ws[i] * ns[i] for i in range(n)]) <= M)
    s.maximize(Sum([vs[i] * ns[i] for i in range(n)]))

    if s.check() == sat:
        m = s.model()
        print([m.eval(ns[i]) for i in range(n)])
    else:
        print("No solution")


kn([1, 2, 3], [1, 3, 5], 8)
