import math


def generate_function(n, a):
    def order_n(x):
        return x**n - a
    return order_n

def generate_function_derivative(n):
    def order_n(x):
        return n*x**(n-1)
    return order_n

def root_tangent(x0, y, m):
    return x0 - y/m

def __recursive_bisection(lower, upper, accuracy, f):
    mid = 0.5 * (upper - lower) + lower

    if (upper - lower) < 10**(-1 * accuracy):
        roundable = mid * 10**(accuracy)
        rounded = round(roundable) / 10**(accuracy)
        return rounded

    if f(mid) > 0:
        return __recursive_bisection(lower, mid, accuracy, f)
    elif f(mid) < 0:
        return __recursive_bisection(mid, upper, accuracy, f)
    else:
        return mid

def calc_root_bisection(a, n, accuracy):
    return __recursive_bisection(0, a, accuracy, generate_function(n, a))

def __recursive_newton(x, f, df, acc):
    tan_root = root_tangent(x, f(x), df(x))
    if x - tan_root < 10**(-1*acc):
        roundable = tan_root * 10**(acc)
        rounded = round(roundable) / 10**(acc)
        return rounded

    return __recursive_newton(tan_root, f, df, acc)
    

def calc_root_newton_rhapson(a, n, accuracy):
    return __recursive_newton(a, generate_function(n, a), generate_function_derivative(n), accuracy)


print(calc_root_bisection(2, 3, 6))
print(calc_root_newton_rhapson(2, 3, 6))

