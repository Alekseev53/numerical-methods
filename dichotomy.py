import numpy as np
def dih(f, l, r, eps=1e-7):
    if f(l) * f(r) > 0:
        return None
    while abs(r - l) > eps:
        m = (l + r) / 2
        if f(m) == 0:
            return m
        elif f(m) * f(l) < 0:
            r = m
        else:
            l = m
    return (l + r) / 2


def find_all_roots(f, range_l, range_r, eps=1e-5, max_roots=100, max_attempts=1000):
    roots = []
    attempts = 0
    while len(roots) < max_roots and attempts < max_attempts:
        l = np.random.uniform(range_l, range_r)
        r = np.random.uniform(range_l, range_r)
        l, r = min(l, r), max(l, r)

        root = dih(f, l, r, eps)
        while root is not None and abs(f(root+eps/10)) < eps:
            roots.append(root)
            f = lambda x, f=f, root=root: f(x) / (x - root) if x != root else 0

        attempts += 1

    return list(roots)


def f(x):
    return (x - 2) * ((x - 3) ** 3) * (x - 7)
    #return (x - 2) * ((x - 3) ** 2) * (x - 7)

roots = find_all_roots(f, -10, 10)
print([round(x,2) for x in roots])
