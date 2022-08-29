from main import Matrix

def add():
    m = Matrix(2,2)
    m.setd([1,1],1)
    n = m.add(Matrix(2,2).setd([1,1],2))

    result = [[1,1],[1,1]]
    if n.all() != result:
        print("Failed add")
    else:
        print("Success on add")

def transpose():
    m = Matrix(3,3)
    m.setd([1,1,1],1)
    m.setd([2,2,2],2)
    n = m.transpose()
    result = [
        [1,0,2],
        [0,2,0],
        [2,0,1]
    ]
    if n.all() != result:
        print("Failed trans")
    else:
        print("Success on trans")

def multiply():
    m = Matrix(3,3)
    m.setd([1,1,1], 1)
    m.switch_row(3, 2)
    result = [
        [1,2,3],
        [7,8,9],
        [4,5,6]
    ]
    n = Matrix(3, 3)
    n.setm(result).switch_row(3,2)
    o = m.matrix_multiply(n)
    if o.all() != result:
        print("Failed mult")
        o.display()
    else:
        print("Success on mult")

add()
transpose()
multiply()

m = Matrix(2,2)
m.setd([2,2],1)
print(m.det())