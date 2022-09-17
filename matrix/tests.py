from matrix import Matrix

def add():
    m = Matrix(2,2)
    m.set_diag([1,1],1)
    n = m.add(Matrix(2,2).set_diag([1,1],2))

    result = [[1,1],[1,1]]
    if n.get_raw() != result:
        print("Failed add")
    else:
        print("Success on add")

def transpose():
    m = Matrix(3,3)
    m.set_row([2,2,2], 0)
    m.set_row([1,1,1], 1)
    m.set_row([9,0,9],2)
    n = m.transpose()
    result = [
        [2,1,9],
        [2,1,0],
        [2,1,9]
    ]
    if n.get_raw() != result:
        print("Failed trans")
    else:
        print("Success on trans")

def multiply():
    m = Matrix(3,3)
    m.set_diag([1,1,1], 1)
    m.switch_row(2, 1)
    result = [
        [1,2,3,4],
        [9,10,11,12],
        [5,6,7,8]
    ]
    n = Matrix(3, 4)
    n.set_raw(result).switch_row(2,1)
    o = m.matrix_multiply(n)
    if o.get_raw() != result:
        print("Failed mult")
        o.display()
        return
    try:
        n.matrix_multiply(m)
    except:
        print("Success on mult")

def det():
    m = Matrix(3,3)
    m.set_raw([
        [3,4,1],
        [9,0,2],
        [0,1,3]
    ])
    result = -105
    if m.det() != result:
        print("Failed det")
        print(m.det())
    else:
        print("Success on det")

def rref():
    m = Matrix(3,3)
    m.set_raw([
        [7,3,35],
        [1,9,5],
        [2,2,10]
    ])
    result = [
        [1,0,5],
        [0,1,0],
        [0,0,0]
    ]
    if m.rref().get_raw() != result:
        print("Failed rref")
        m.rref().display()
    else:
        print("Success on rref")

def inverse():
    success = True

    m = Matrix(3,3)
    m.set_raw([
        [1,2,3],
        [2,4,6],
        [7,7,7]
    ])

    print(m.det())

    m = Matrix(3,3)
    m.set_raw([
        [1,2,3],
        [2,4,6],
        [3,6,9]
    ])
    if m.inverse().get_raw() != result:
        print("Failed inverse")
        m.inverse().display()
    else:
        print("Success on inverse")

def rrefdet():
    m = Matrix(3,3)
    m.set_raw([
        [8,19,3],
        [4,10,7],
        [6,3,12]
    ])
    # compare Matrix.rref_det() to Matrix.det() within reasonable error
    if abs(m.rref_det() - m.det()) > 0.0000000000001:
        print("Failed rrefdet")
        print(m.rref_det())
        print(m.det())

    
rref()
inverse()
rrefdet()
add()
transpose()
multiply()
det()

m = Matrix(3,3)
m.set_raw([
    [2,8,3],
    [4,5,6],
    [7,8,9]
])
# m.matrix_multiply(m.inverse()).display()

