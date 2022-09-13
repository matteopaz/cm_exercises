import math

def f1(r, derivative):
    x = r[0]
    y = r[1]
    if derivative == 0:
        return (x - 1)**2 + 3*y**2
    elif derivative == 1:
        return [2*x - 2, 6*y]
    else:
        raise Exception("didnt do this lol") 

def f2(r, derivative):
    x = r[0]
    y = r[1]
    if derivative == 0:
        return y**2 + y * math.cos(x)
    elif derivative == 1:
        return [y * math.sin(x), 2*y + math.cos(x)]
    else:
        raise Exception("didnt do this lol")

def f3(r, derivative):
    x = r[0]
    y = r[1]
    z = r[2]
    if derivative == 0:
        return (x-1)**2 +3*(y-2)**2 + 4*(z+1)**2
    elif derivative == 1:
        return [2*x - 2, 6*y - 12, 8*z + 8]
    else:
        raise Exception("didnt do this lol")

def f4(r, derivative):
    x = r[0]
    y = r[1]
    z = r[2]
    if derivative == 0:
        return x**2 + 3*y**2 + 4*z**2 + math.cos(x*y*z)
    elif derivative == 1:
        return [2*x - y*z*math.sin(x*y*z), 6*y - x*z*math.sin(x*y*z), 8*z - x*y*math.sin(x*y*z)]
    else:
        raise Exception("didnt do this lol")

learning_rate = 0.1

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

print(gradient_descent([0,0], f1))
print(gradient_descent([0,0], f2))
print(gradient_descent([0,0,0], f3))
print(gradient_descent([0,0,0], f4))