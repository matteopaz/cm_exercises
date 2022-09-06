
def f(x, n):
    return x**n - a

def df(x, n):
    return n*x**(n-1)

def root_tangent(x0, y, m):
    return x0 - y/m

def __recursive_bisection(upper, lower, n, accuracy):

    mid = 0.5 * (upper - lower) + lower

    if (mid - lower) < 10**(-1 * accuracy):
        return mid

    if f(mid, n) > 0:
        return bisection(lower, mid, accuracy)
    elif f(mid, n) < 0:
        return bisection(mid, upper, accuracy)
    else:
        return mid

def calc_root_bisection(a, n, accuracy):
    return __recursive_bisection(0, a, n, accuracy)

print(calc_root_bisection(2, 2, 3))
