from matrix import Matrix
import math

digits = [1,2,3,4,5,6,7,8,9]

def adds_to(arr, n):
    arrsum = 0
    for i in range(len(arr)):
        arrsum += arr[i]
    return (arrsum == n)


def is_valid(matrix):
    dim = matrix.get_dim()
    for r in range(dim[0]):
        row = matrix.get_row(r)
        if not adds_to(row, 15):
            return False
    for c in range(dim[1]):
        col = matrix.get_col(c)
        if not adds_to(col, 15):
            return False
    diag1 = matrix.get_diag(1)
    diag2 = matrix.get_diag(2)

    if not adds_to(diag1, 15) or not adds_to(diag2, 15):
        return False    
    
    return True

def is_hopeless(matrix):
    for i in range(3):
        row = matrix.get_row(i)
        col = matrix.get_col(i)

        colsum = 0
        rowsum = 0
        for e in row:
            if not e:
                rowsum = 15 # Pretend row is valid if not filled
                break
            rowsum += e
            
        if rowsum != 15:
            return True

        for e in col:
            if not e:
                colsum = 15
                break
            colsum += e
        
        if colsum != 15:
            return True

    diag1 = matrix.get_diag(1)
    diag2 = matrix.get_diag(2)
    dsum1 = 0
    dsum2 = 0

    for e in diag1:
        if not e:
            dsum1 = 15
            break
        dsum1 += e
    
    if dsum1 != 15:
        return True    

    for e in diag2:
        if not e:
            dsum2 = 15
            break
        dsum2 += e

    if dsum2 != 15:
        return True  

    return False    


def remove(vals, arr):
    new = []
    for e in arr:
        new.append(e)
    for val in vals:
        new.remove(val)
    return new

def place(vals, matrix):
    matrix.fill(None)
    for i in range(len(vals)):
        matrix.set_el(vals[i], math.floor(i/3), i % 3)

sq = Matrix(3,3)

# for num1 in digits:
#     place([num1], sq)

#     for num2 in remove([num1], digits):
#         place([num1,num2], sq)
        
#         for num3 in remove([num1, num2], digits):
#             place([num1,num2,num3], sq)

#             for num4 in remove([num1, num2, num3], digits):
#                 place([num1,num2,num3,num4], sq)

#                 for num5 in remove([num1, num2, num3, num4], digits):
#                     place([num1,num2,num3,num4,num5], sq)

#                     for num6 in remove([num1, num2, num3, num4, num5], digits):
#                         place([num1,num2,num3,num4,num5,num6], sq)

#                         for num7 in remove([num1, num2, num3, num4, num5, num6], digits):
#                             place([num1,num2,num3,num4,num5,num6,num7], sq)

#                             for num8 in remove([num1, num2, num3, num4, num5, num6, num7], digits):
#                                 place([num1,num2,num3,num4,num5,num6,num7,num8], sq)

#                                 for num9 in remove([num1, num2, num3, num4, num5, num6, num7, num8], digits):
#                                     place([num1,num2,num3,num4,num5,num6,num7,num8,num9], sq)

#                                     if is_valid(sq):
#                                         sq.display()

for num1 in digits:
    place([num1], sq)
    if is_hopeless(sq):
        continue

    for num2 in remove([num1], digits):
        place([num1,num2], sq)
        if is_hopeless(sq):
            continue
        
        
        for num3 in remove([num1, num2], digits):
            place([num1,num2,num3], sq)
            if is_hopeless(sq):
                continue

            for num4 in remove([num1, num2, num3], digits):
                place([num1,num2,num3,num4], sq)
                if is_hopeless(sq):
                    continue

                for num5 in remove([num1, num2, num3, num4], digits):
                    place([num1,num2,num3,num4,num5], sq)
                    if is_hopeless(sq):
                        continue    

                    for num6 in remove([num1, num2, num3, num4, num5], digits):
                        place([num1,num2,num3,num4,num5,num6], sq)
                        if is_hopeless(sq):
                            continue

                        for num7 in remove([num1, num2, num3, num4, num5, num6], digits):
                            place([num1,num2,num3,num4,num5,num6,num7], sq)
                            if is_hopeless(sq):
                                continue

                            for num8 in remove([num1, num2, num3, num4, num5, num6, num7], digits):
                                place([num1,num2,num3,num4,num5,num6,num7,num8], sq)
                                if is_hopeless(sq):
                                    continue

                                for num9 in remove([num1, num2, num3, num4, num5, num6, num7, num8], digits):
                                    place([num1,num2,num3,num4,num5,num6,num7,num8,num9], sq)
                                    if is_hopeless(sq):
                                        continue

                                    sq.display()