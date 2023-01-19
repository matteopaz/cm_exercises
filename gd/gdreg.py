import math
import matplotlib.pyplot as plt
learning_rate = 0.001

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

def gradient_descent(r, f, iter):

    for i in range(iter):
        # print("current fit:", r,"\n RSS:", f(r,0)," \n GradRSS:", f(r,1))
        try:
           adjustor = mult(f(r,1), -learning_rate)
        except:
            print("Divergent")
            return
        r = add(r, adjustor)
    return r

def generalfit(fs, bestfit, data, xmin=0, xmax=10, res=100):
    for pt in data:
        plt.plot(pt[0], pt[1], "r.")
    
    x = [xpt / res for xpt in range(xmin*res, xmax*res)]
    def eval(x):
        sum = 0
        for i in range(len(fs)):
            sum += bestfit[i] * fs[i](x)
        return sum
    
    y = [eval(xpt) for xpt in x]
    print(x,y)
    plt.plot(x, y)
    # plt.show()
datarss0 = [(0.001,0.01),(2,4),(3,9)]
def RSS0(r, derivative):
    a = r[0]
    b = r[1]
    if derivative == 0:
        sum = 0
        for pt in datarss0:
            y = pt[1]
            x = pt[0]
            sum += (y - (a*(x**b)))**2
        return sum
    if derivative == 1:
        sum = [0,0]
        for pt in datarss0:
            y = pt[1]
            x = pt[0]
            sum[0] += 2*(y - (a*(x**b)))*(-x**b)
            sum[1] += 2*(y - (a*(x**b)))*(-a*(x**b)*math.log(x))
        return sum

# sol = gradient_descent([1,1], RSS0, 10000)
# print(sol)
# for pt in datarss0:
#     plt.plot(pt[0],pt[1], "r.")
x = [xpt / 100 for xpt in range(0, 1000)]
# y = [sol[0]*(xpt**sol[1]) for xpt in x]
# plt.plot(x,y)
# plt.show()

datarss1 = [(0.001,0.001),(2,4),(3,9)]
def RSS1(r ,derivative):
    a = r[0]
    b = r[1]
    c = r[2]
    if derivative == 0:
        sum = 0
        for pt in datarss1:
            y = pt[1]
            x = pt[0]
            sum += (y - (a*(x**2) + b*x + c))**2
        return sum
    elif derivative == 1:
        sum = [0,0,0]
        for pt in datarss1:
            y = pt[1]
            x = pt[0]
            sum[0] += 2*(y - (a*(x**2) + b*x + c))*(-x**2)
            sum[1] += 2*(y - (a*(x**2) + b*x + c))*(-x)
            sum[2] += 2*(y - (a*(x**2) + b*x + c))*(-1)
        return sum

# sol1 = gradient_descent([1,1,1], RSS1, 10000)
# print(sol1)
# y1 = [sol1[0]*(xpt**2) + sol1[1]*xpt + sol1[2] for xpt in x]
# for pt in datarss1:
#     plt.plot(pt[0],pt[1], "r.")
# plt.plot(x,y1)
# plt.show()

datarss2 = [(1,1), (2,1), (3,2)]
def RSS2(r, derivative):
    a = r[0]
    b = r[1]
    if derivative == 0:
        sum = 0
        for pt in datarss2:
            y = pt[1]
            x = pt[0]
            e = math.exp(-(a*x + b))
            sum += (y - (5 / (1 + e) + 0.5))**2
        return sum
    elif derivative == 1:
        sum = [0,0]
        for pt in datarss2:
            y = pt[1]
            x = pt[0]
            e = math.exp(-(a*x + b))
            sum[0] += 2*(y - (5 / (1 + e) + 0.5))*(5*x*e / (e + 1)**2)*-1
            sum[1] += 2*(y - (5 / (1 + e) + 0.5))*(5*e / (e + 1)**2)*-1
        return sum

# sol2 = gradient_descent([1,1], RSS2, 10000)
# print(sol2)
# y2 = [5 / (1 + math.exp(-(sol2[0]*xpt + sol2[1]))) + 0.5 for xpt in x]
# for pt in datarss2:
#     plt.plot(pt[0],pt[1], "r.")
# plt.plot(x,y2)
# plt.show()

datarss3 = [(0,0),(5,2),(1,-1),(6,-4),(2,2),(7,4),(3,0),(8,1),(4,0),(9,-3)]
def RSS3(r, derivative):
    a = r[0]
    b = r[1]
    c = r[2]
    d = r[3]
    f = lambda x: a*math.sin(b*x) + c*math.sin(d*x)
    if derivative == 0:
        sum = 0
        for pt in datarss3:
            y = pt[1]
            x = pt[0]
            sum += (y - f(x))**2
        return sum
    elif derivative == 1:
        sum = [0,0,0,0]
        for pt in datarss3:
            y = pt[1]
            x = pt[0]
            sum[0] += 2*(y - f(x))*(math.sin(b*x))*-1
            sum[1] += 2*(y - f(x))*(a*x*math.cos(b*x))*-1
            sum[2] += 2*(y - f(x))*(math.sin(d*x))*-1
            sum[3] += 2*(y - f(x))*(c*x*math.cos(d*x))*-1
        return sum
sol3 = gradient_descent([0.1,-0.1,0.2,-0.3], RSS3, 10000)
print(sol3)
y3 = [sol3[0]*math.sin(sol3[1]*xpt) + sol3[2]*math.sin(sol3[3]*xpt) for xpt in x]
for pt in datarss3:
    plt.plot(pt[0],pt[1], "r.")
plt.plot(x,y3)
plt.show()