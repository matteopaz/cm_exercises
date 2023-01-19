import matplotlib.pyplot as plt

def copy(arr):
    new = []
    for e in arr:
        new.append(e)
    return new

def quick_sort(array, sortindex):
    arr = copy(array)
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    left = []
    right = []
    for e in arr:
        if e[sortindex] < pivot[sortindex]:
            left.append(e)
        else:
            right.append(e)
    return quick_sort(left, sortindex) + [pivot] + quick_sort(right, sortindex)

def dist(a, b):
    d = [x - y for x, y in zip(a, b)]
    return sum([x**2 for x in d]) ** 0.5


#format: datapt is an array, 0: Type, rest is position
def knn(pos, data, k):
    dists = []
    for pt in data:
        dists.append(dist(pos, pt[1:]))
    extdata = [[dists[i]] + data[i] for i in range(len(data))]
    extdata = quick_sort(extdata, 0)
    knearest = extdata[:k]
    types = {}
    for pt in knearest:
        if pt[1] not in types:
            types[pt[1]] = 0
        types[pt[1]] += 1
    print(types)
    maxtype = None
    maxseen = 0
    for type in types:
        if types[type] > maxseen:
            maxtype = type
            maxseen = types[type]
    print(maxtype, maxseen)


    return maxtype


def cval(k, data):
    correct = 0
    for i in range(len(data)):
        newdata = data[:i] + data[i+1:]
        test = data[i]
        result = knn(test[1:], newdata, k)
        if result == test[0]:
            correct += 1
    return correct / len(data)




data0 = [
    ["Shortbread", 0.15, 0.2],
    ["Shortbread", 0.15, 0.3],
    ["Shortbread", 0.2, 0.25],
    ["Shortbread", 0.25, 0.4],
    ["Shortbread", 0.3, 0.35],
    ["Sugar", 0.05, 0.25],
    ["Sugar", 0.05, 0.35],
    ["Sugar", 0.1, 0.3],
    ["Sugar", 0.15, 0.4],
    ["Sugar", 0.25, 0.35]
]

data1 = [
    ["Shortbread", 0.6, 200],
    ["Shortbread", 0.6, 300],
    ["Shortbread", 0.8, 250],
    ["Shortbread", 1.0, 400],
    ["Shortbread", 1.2, 350],
    ["Sugar", 0.2, 250],
    ["Sugar", 0.2, 350],
    ["Sugar", 0.4, 300],
    ["Sugar", 0.6, 400],
    ["Sugar", 1.0, 350]
]

data2 = [
    ["Shortbread", 0.4, 0],
    ["Shortbread", 0.4, 0.5],
    ["Shortbread", 0.6, 0.25],
    ["Shortbread", 0.8, 1],
    ["Shortbread", 1.0, 0.75],
    ["Sugar", 0, 0.25],
    ["Sugar", 0, 0.75],
    ["Sugar", 0.2, 0.5],
    ["Sugar", 0.4, 1],
    ["Sugar", 0.8, 0.75]
]

k = 3
plotset = data2
# for pt in plotset:
#     type = pt[0]
#     disp = "g."
#     if type == "Shortbread":
#         disp = "rx"
#     plt.plot(pt[1], pt[2], disp)

# pt = [0.13, 0.35]
# pred = knn(pt, plotset, k)
# disp = "go"
# if pred == "Shortbread":
#     disp = "ro"

# plt.plot(pt[0], pt[1], disp)


# plt.plot(pt[0], pt[1], "ro")

x = range(10)
y = [cval(xt, plotset) for xt in x]
plt.plot(x, y, "-r.")
plt.show()