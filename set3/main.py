def one_reg(n):
    prev = 5
    arr = []
    for i in range(n):
        arr.append(prev)
        prev = 3 * prev - 4
    return arr

def one_rec(n):
    if n == 1:
        return 5
    else:
        prev = one_rec(n - 1)
        return 3 * prev - 4

def two_reg(n):
    prev = 25
    arr = []
    for i in range(n):
        arr.append(prev)
        if prev % 2:
            prev = 3 * prev + 1
        else:
            prev = prev / 2
    return arr

def two_rec(n):
    if n == 1:
        return 25
    else:
        prev = two_rec(n - 1)
        if prev % 2:
            return 3 * prev + 1
        else:
            return prev // 2

def thr_reg(n):
    arr = [0, 1]
    if n < 3:
        return arr
    for i in range(2, n):
        arr.append(arr[i - 2] + arr[i - 1])
    return arr    

def thr_rec(n):
    def inner(n):
        if n == 1:
            return [0, 1]
        else:
            prev = inner(n - 1)
            return [prev[1] , prev[0] + prev[1]]
    return inner(n - 1)[1]

def fr_reg(n):
    arr = [2, -3]
    if n < 3:
        return arr
    for i in range(2, n):
        arr.append(arr[i - 2] * arr[i - 1] + arr[i-1])
    return arr   

def fr_rec(n):
    def inner(n):
        if n == 1:
            return [2, -3]
        else:
            prev = inner(n - 1)
            return [prev[1] , prev[0] * prev[1] + prev[1]]
    return inner(n - 1)[1]

print(one_reg(10), one_rec(10))
print(two_reg(10), two_rec(10))
print(thr_reg(10), thr_rec(10))
print(fr_reg(7), fr_rec(7))

