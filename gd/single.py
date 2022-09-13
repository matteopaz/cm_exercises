import math

def f1(x, derivative):
    if derivative == 0:
        return x**2 + x + 1
    elif derivative == 1:
        return 2*x+1
    else:
        raise Exception("didnt define that lol")

def f2(x, derivative):
    if derivative == 0:
        return -x**4 + x**3 - x**2
    elif derivative == 1:
        return -4 * x**3 + 3*x**2 - 2*x
    else:
        raise Exception("didnt define that lol")

def f3(x, derivative):
    if derivative == 0:
        return (math.sin(x) / (1 + x**2))
    elif derivative == 1:
        return (math.cos(x)*(1+x**2) - 2*x*math.sin(x)) / (1+x**2)**2
    else:
        raise Exception("didnt define that lol")

def f4(x, derivative):
    if derivative == 0:
        return 3*math.cos(x) + x**2 * math.exp(math.sin(x))
    elif derivative == 1:
        return (-3*math.sin(x)   +   2*x*math.exp(math.sin(x))  +   x**2 * math.cos(x) * math.exp(math.sin(x)))
    else:
        raise Exception("didnt define that lol")


learning_rate = 0.1

def gradient_descent(x, f):
    adjustor = 0
    try:
        adjustor = learning_rate*f(x,1)
    except:
        print("Divergent")
        return
    if abs(adjustor) <= learning_rate*0.001:
        return [x, f(x,0)]
    return gradient_descent(x-adjustor, f)

print(gradient_descent(0,f1))
print(gradient_descent(1,f2))
print(gradient_descent(1,f3))
print(gradient_descent(0,f3))
print(gradient_descent(0.1,f4))
print(gradient_descent(-0.1,f4))
