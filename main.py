from z3 import *


def zerosum(xs):
    """
    In computer science, the subset sum problem is an important decision problem in complexity theory
    and cryptography. There are several equivalent formulations of the problem. One of them is: given a
    set (or multiset) of integers, is there a non-empty subset whose sum is zero? For example, given the
    set {−7, −3, −2, 9000, 5, 8}, the answer is yes because the subset {−3, −2, 5} sums to zero.
    """
    n = len(xs)

    ss = [Bool(f"ss[{i}]") for i in range(n)]

    s = Optimize()

    binary_activation = Sum([If(ss[i], xs[i], 0) for i in range(n)]) == 0
    length = Sum([If(ss[i], 1, 0) for i in range(n)])

    s.add(binary_activation)
    s.maximize(length)

    if s.check() == sat:
        m = s.model()
        print([xs[i] for i in range(n) if m.eval(ss[i])])
    else:
        print("No solution")


def kn(ws, vs, M):
    """
    Given a list of items which might be packed, each of which has a weight and a value (both non-negative real
    numbers), pick the items with the greatest total value that do not exceed a given capacity of the knapsack w.
    """
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


def mss(xs):
    """
    Given a list of integers, find the (contiguous) segment that has maximal sum. E.g.: the maximum sum segment
    of [2, -3, 4, -1, 3] is [4, -1, 3].
    """
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


def sort(xs):
    n = len(xs)

    ns = [Int(f"ns[{i}]") for i in range(n)]
    s = Solver()

    value_in_xs = [Or([ns[i] == xs[j] for i in range(n)]) for j in range(n)]

    value_between_l_r = [ns[i] <= ns[i + 1] for i in range(n - 1)]

    same_duplicates = [
        Sum([If(xs[i] == ns[j], 1, 0) for j in range(n)]) == Sum([If(xs[i] == xs[j], 1, 0) for j in range(n)]) for i in
        range(n)]

    s.add(same_duplicates)
    s.add(value_in_xs)
    s.add(value_between_l_r)

    if s.check() == sat:
        m = s.model()
        print([m.eval(ns[i]) for i in range(n)])
    else:
        print("No solution")


def wp(xs):
    """
    Given a list, a peak is a subsegment composed of an increasing segment, directly followed by a decreasing one.
    Find a widest peak of a given list. For example, the widest peak of [3, 2, 1, 2, 3, 2, 1, 2] is [1, 2, 3, 2, 1].
    """
    n = len(xs)
    s = Optimize()
    ns = [Bool(f"ns[{i}]") for i in range(n)]

    edge_valleys = [If(xs[0] < xs[1], True, False), If(xs[n - 1] < xs[n - 2], True, False)]
    valleys = [If(And(xs[i] < xs[i - 1], xs[i] < xs[i + 1]), True, False) for i in range(1, n - 1)]
    print([edge_valleys[0]] + valleys + [edge_valleys[1]])


    maximizer = [Sum([ns[i] for i in range(n)])]

    s.

    if s.check() == sat:
        m = s.model()
        print([m.eval(ns[i]) for i in range(n)])
    else:
        print("No solution")


def wv():
    """
    In a list, a “valley” is a segment in which all the elements are at most equal to the ends (the “walls”). Find a
    longest valley. For example, the longest valley in the list [3, 2, 1, 2, 3, 2, 1, 2] is [3, 2, 1, 2, 3]
    """
    pass


# zerosum([-7, 7, -3, -2, -3, 9000, 5, 8])
# kn([1, 2, 3], [1, 3, 5], 8)
# mss([0, -2, 5, 5, -7, 2])
# sort([9, 8, 2, 3, 5, 6, 12, 9, 9])
wp([1, 2, 4, 3, 1, 3])
