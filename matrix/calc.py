from matrix import Matrix

m = Matrix(2,2)
m.set_raw([
    [2, 3],
    [0, 0]
])
print(m.is_in_span([3,1], m.img()))