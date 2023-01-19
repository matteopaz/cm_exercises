from numerical_deriv import numerical_derivative
import math

def add(a,b):
    new = []
    for i in range(len(a)):
        new.append(a[i]+b[i])
    return new

def dot(a,b):
    new = []
    for i in range(len(a)):
        new.append(a[i]*b[i])
    return new

def mult(a,b):
    new = []
    for i in range(len(a)):
        new.append(a[i]*b)
    return new

def mag(r):
    pre_sq = 0
    for v in r:
        pre_sq += v**2
    return math.sqrt(pre_sq)

def gradient_descent(r, f):
    try:
        adjustor = mult(f(r,1), learning_rate)
    except:
        print("Divergent")
        return

    if mag(adjustor) <= learning_rate * 0.001:
        return [r, f(r,0)]
    
    return gradient_descent(add(r, mult(adjustor, -1)), f)