from matrix import Matrix
import matplotlib.pyplot as plt
import math

data1 = {
    "co": Matrix(3,2).set_raw([[1,1],[3,1],[4,1]]),
    "sol": Matrix(3,1).set_raw([[0],[-1],[5]])
}

data2 = {
    "co": Matrix(4,2).set_raw([[-2,1],[1,1],[3,1], [4,1]]),
    "sol": Matrix(4,1).set_raw([[3],[0],[-1],[5]])
}

data3 = {
    "co": Matrix(4,3).set_raw([[4,-2,1],[1,1,1],[9,3,1],[16,4,1]]),
    "sol": Matrix(4,1).set_raw([[3],[0],[-1],[5]])
}

data4 = {
    "co": Matrix(5,3).set_raw([[9, -3, 1], [4, -2, 1], [1, 1, 1], [9, 3, 1], [16, 4, 1]]),
    "sol": Matrix(5,1).set_col([-4, 3, 0, -1, 5], 0)
}

data5 = {
    "co": Matrix(5,4).set_raw([
        [-27, 9, -3, 1],
        [-8, 4, -2, 1],
        [1, 1, 1, 1],
        [27, 9, 3, 1],
        [64, 16, 4, 1]
        ]),
    "sol": Matrix(5,1).set_col([-4, 3, 0, -1, 5], 0)
}

data6 = {
    "co": Matrix(3,2).set_raw([
        [0.6931, 1],
        [1.3863, 0.333],
        [1.609, 0.25]
        ]),
    "sol": Matrix(3,1).set_col([0,-1,5], 0)
}
data7 = {
    "co": Matrix(3,2).set_raw([
        [0.5, 0.5],
        [0.375, 0.125],
        [0.25, 0.0625]
        ]),
    "sol": Matrix(3,1).set_col([0,-1,5], 0)
}
data8 = {
    "co": Matrix(3,2).set_raw([
        [3, 1],
        [27, 1.4422],
        [81, 1.5874]
        ]),
    "sol": Matrix(3,1).set_col([0,-1,5], 0)
}
data9 = {
    "co": Matrix(4,2).set_raw([
        [-18, 2],
        [0, 2],
        [3, 4],
        [100, 512]
        ]),
    "sol": Matrix(4,1).set_col([-3,-4,2,3], 0)
}
data10 = {
    "co": Matrix(4,2).set_raw([
        [0,1],
        [1,1],
        [2,1],
        [3,1]
        ]),
    "sol": Matrix(4,1).set_col([5,7.5,8,8.3], 0)
}

# bestfit1 = data1["co"].pseudoinverse().matrix_multiply(data1["sol"])
# bestfit2 = data2["co"].pseudoinverse().matrix_multiply(data2["sol"])
# bestfit3 = data3["co"].pseudoinverse().matrix_multiply(data3["sol"])
# bestfit4 = data4["co"].pseudoinverse().matrix_multiply(data4["sol"])
# bestfit5 = data5["co"].pseudoinverse().matrix_multiply(data5["sol"])
# bestfit6 = data6["co"].pseudoinverse().matrix_multiply(data6["sol"])
# bestfit7 = data7["co"].pseudoinverse().matrix_multiply(data7["sol"])
# bestfit8 = data8["co"].pseudoinverse().matrix_multiply(data8["sol"])
# bestfit9 = data9["co"].pseudoinverse().matrix_multiply(data9["sol"])
bestfit10 = data10["co"].pseudoinverse().matrix_multiply(data10["sol"])

# plot a line with m and b as variables and a range variable
def plot_line(m, b, range, pts):
    x = range
    y = [m * i + b for i in x]
    plt.plot(x, y)

    for pt in pts:
        plt.plot(pt[0], pt[1], 'ro')



def plot_quadratic(a, b, c, range, pts):
    x = range
    y = [a * i**2 + b * i + c for i in x]
    plt.plot(x, y)

    for pt in pts:
        plt.plot(pt[0], pt[1], 'ro')



def plot_cubic(a, b, c, d, range, pts):
    x = range
    y = [a * i**3 + b * i**2 + c * i + d for i in x]
    plt.plot(x, y)

    for pt in pts:
        plt.plot(pt[0], pt[1], 'ro')


# plot_line(bestfit1.get_el(0,0), bestfit1.get_el(1,0), range(-20, 20), [[1,0], [3,-1], [4,5]])
# plot_line(bestfit2.get_el(0,0), bestfit2.get_el(1,0), range(-20, 20), [[-2,3], [1,0], [3,-1], [4,5]])
# plot_quadratic(bestfit3.get_el(0,0), bestfit3.get_el(1,0), bestfit3.get_el(2,0), range(-10, 10), [[-2,3], [1,0], [3,-1], [4,5]])
# plot_quadratic(bestfit4.get_el(0,0), bestfit4.get_el(1,0), bestfit4.get_el(2,0), range(-10, 10), [[-3,-4], [-2,3], [1,0], [3,-1], [4,5]])
# plot_cubic(bestfit5.get_el(0,0), bestfit5.get_el(1,0), bestfit5.get_el(2,0), bestfit5.get_el(3,0), range(-7, 7), [[-3,-4], [-2,3], [1,0], [3,-1], [4,5]])

# x6 = [0.2*u + 0.2 for u in range(0, 50)]
# y6 = [bestfit6.get_el(0,0)*math.log(u + 1) + bestfit6.get_el(1,0) / u for u in x6]
# pts6 = [(1,0), (3,-1), (4,5)]

# for pt in pts6:
#     plt.plot(pt[0], pt[1], 'ro')
# plt.plot(x6, y6)
# plt.show()

# x7 = [0.2*u + 0.2 for u in range(0, 50)]
# y7 = [(bestfit7.get_el(0,0)*u + bestfit7.get_el(1,0)) / (2**u) for u in x7]
# pts7 = [(1,0), (3,-1), (4,5)]

# for pt in pts7:
#     plt.plot(pt[0], pt[1], 'ro')
# plt.plot(x7, y7)
# plt.show()

# x8 = [0.2*u + 0.2 for u in range(0, 30)]
# y8 = [bestfit8.get_el(0,0)*3**u + bestfit8.get_el(1,0)*u**(1 / 3) for u in x8]
# pts8 = [(1,0), (3,-1), (4,5)]

# for pt in pts8:
#     plt.plot(pt[0], pt[1], 'ro')
# plt.plot(x8, y8)
# plt.show()

# x9 = [0.2*u + 0.2 for u in range(0, 30)]
# y9 = [bestfit9.get_el(0,0)*u**3 + bestfit9.get_el(1,0)*u**2 + bestfit9.get_el(2,0)*u + bestfit9.get_el(3,0) for u in x9]
# print(bestfit9.get_el(0,0), bestfit9.get_el(1,0))

pts9 = [(0,5), (1,7.5),(2,8),(3,8.3)]
bestfit10.display()

for pt in pts9:
    plt.plot(pt[0], pt[1], 'ro')
plot_line(bestfit10.get_el(0,0), bestfit10.get_el(1,0), range(-10, 10), pts9)
plt.show()