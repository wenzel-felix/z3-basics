from z3 import *


def zerosum(xs):
    n = len(xs)

    ss = [Bool(f"ss[{i}]") for i in range(n)]

    s = Optimize()

    binary_activation = Sum([If(ss[i], xs[i], 0) for i in range(n)]) == 0
    print(binary_activation)
    length = Sum([If(ss[i], 1, 0) for i in range(n)])
    print(length)

    s.add(binary_activation)
    s.maximize(length)

    if s.check() == sat:
        m = s.model()
        print([xs[i] for i in range(n) if m.eval(ss[i]) is True])
    else:
        print("No solution")


zerosum([-7, 7, -3, -2, -3, 9000, 5, 8])


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


def mss(xs):
    n = len(xs)

    l, r = Ints("l r")
    s = Optimize()

    s.add(l < r, l >= 0, r < n)
    s.maximize(Sum([If(And(l <= i, r >= i), xs[i], 0) for i in range(n)]))

    if s.check() == sat:
        m = s.model()
        l = m.eval(l).as_long()
        r = m.eval(r).as_long()
        print([xs[i] for i in range(l, r + 1)])
    else:
        print("No solution")


mss([0, -2, 5, 5, -7, 2])


# Bonus: sort with duplicates
def sort(xs):
    n = len(xs)

    ns = [Int(f"ns[{i}]") for i in range(n)]
    s = Solver()

    value_in_xs = [Or([ns[i] == xs[j] for i in range(n)]) for j in range(n)]

    value_between_l_r = [ns[i] <= ns[i + 1] for i in range(n-1)]

    same_duplicates = [Sum([If(xs[i] == ns[j], 1, 0) for j in range(n)]) == Sum([If(xs[i] == xs[j], 1, 0) for j in range(n)]) for i in range(n)]

    s.add(same_duplicates)
    s.add(value_in_xs)
    s.add(value_between_l_r)

    if s.check() == sat:
        m = s.model()
        print([m.eval(ns[i]) for i in range(n)])
    else:
        print("No solution")


sort([9, 8, 2, 3, 5, 6, 12, 9, 9])
