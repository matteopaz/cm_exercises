from ast import IsNot
from select import select


class Matrix:


    def __init__(self, rows, cols, start_elem=0):
        self.raw = []
        self.rows = rows
        self.cols = cols
        for i in range(self.rows):
            self.raw.append([start_elem] *self.cols)     
    
    # GETTERS START
    def get_el(self, r, c):
        return self.raw[r][c]

    def get_row(self, n):
        new = []
        for c in range(self.cols):
            new.append(self.get_el(n, c))
        return new
    
    def get_col(self, n):
        new = []
        for r in range(self.rows):
            new.append(self.get_el(r, n))
        return new

    def get_diag(self, diagonal_number=1): 
        if self.rows != self.cols:
            raise Exception("Diagonal not defined for rect matrix") 
        dim = self.rows
        diag = []

        if diagonal_number == 1: # Main
            for i in range(dim):
                diag.append(self.get_el(i,i))
        if diagonal_number == 2: # Other diagonal
            for i in range(dim):
                diag.append(self.get_el(dim - 1 - i, i))
        return diag
    
    def get_dim(self):
        return [int(self.rows), int(self.cols)]
    
    def get_raw(self):
        new = []
        for r in range(self.rows):
            new.append(self.get_row(r))
        return new
    
    # GETTERS END
    # SETTERS START

    def set_el(self, val, r, c):
        self.raw[r][c] = val
        return self

    
    def set_row(self, val, r):
        if not isinstance(val, list):
            raise Exception("Use a list when setting rows/cols")
        if len(val) != self.cols:
            raise Exception("Set list length not equal to matrix dimension")
        self.raw[r] = val
        return self

    def set_col(self, val, c):
        if not isinstance(val, list):
            raise Exception("Use a list when setting rows/cols")
        if len(val) != self.rows:
            raise Exception("Set list length not equal to matrix dimension")

        for r in range(len(self.raw)):
            self.raw[r][c] = val[r]
        return self
        
    def set_diag(self, val, diag_n):
        if self.rows != self.cols:
            raise Exception("Diagonal not defined for rect matrix")

        dim = self.rows

        if not isinstance(val, list):
            raise Exception("Use a list when setting rows/cols")
        if len(val) != dim:
            raise Exception("Set list length not equal to matrix dimension")

        if diag_n == 1: # Main
            for i in range(dim):
                self.raw[i][i] = val[i]
        if diag_n == 2: # Other diag
            for i in range(dim):
                self.raw[dim - 1 -i][i] = val[i]
        return self
    
    def fill(self, val):
        for r in range(self.rows):
            for c in range(self.cols):
                self.set_el(val, r, c)
        return self

    def set_raw(self, m):
        if len(m) != self.rows or len(m[0]) != self.cols:
            raise Exception("Matrix dimension mismatch")
        for r in range(self.rows):
            for c in range(self.cols):
                self.set_el(m[r][c], r, c)
        return self

    # SETTERS OVER

    # SCALAR OPERATIONS 

    def scalar_multiply(self, n):
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                val = self.get_el(r, c) * n
                new.set_el(val, r, c)
        return new

    # SCALAR OPERATIONS END

    # MATRIX ON MATRIX OPERATIONS START

    def add(self, adder):
        if not isinstance(adder, Matrix):
            raise Exception("Please use matrix of same dimension")
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                val = self.get_el(r, c) + adder.get_el(r, c)
                new.set_el(val, r, c)
        return new
    
    def subtract(self, m):
        return self.add(m.scalar_multiply(-1))

    def matrix_multiply(self, mult):
        if not isinstance(mult, Matrix):
            raise Exception("Cannot multiply matrix by non matrix type, try scalar_multiply")

        multdim = mult.get_dim()
        if self.cols != multdim[0]:
            raise Exception("Matrix multiplication incompatible")

        new = Matrix(self.rows, multdim[1], 0)
        for r in range(self.rows):
            row = self.get_row(r)
            for c in range(multdim[1]):
                multcol = mult.get_col(c)
                val = 0
                for el in range(len(row)):
                    val += row[el] * multcol[el]
                new.set_el(val, r, c)
        new.__clean_zeroes()
        return new
    
    # MATRIX ON MATRIX OPERATIONS END


    # ROW OPERATIONS START

    def transpose(self):
        if self.rows != self.cols:
            raise Exception("Diagonal not defined for rect matrix")
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                new.set_el(self.get_el(r,c), c, r)
        return new
    
    def switch_row(self, rownum_one, rownum_two):
        prev = self.get_row(rownum_one)
        next = self.get_row(rownum_two)
        self.set_row(next, rownum_one)
        self.set_row(prev, rownum_two)
        return self
    
    def switch_col(self, colnum_one, colnum_two):
        prev = self.get_col(colnum_one)
        next = self.get_col(colnum_two)
        self.set_col(next, colnum_one)
        self.set_col(prev, colnum_two)
        return self    
    
    def delete_row(self, r):
        new = Matrix(self.rows - 1, self.cols)
        current_row = 0
        for i in range(self.rows):
            if i == r:
                continue
            new.set_row(self.get_row(i), current_row)
            current_row += 1
        return new        

    def delete_col(self, c):
        new = Matrix(self.rows, self.cols - 1)
        current_col = 0
        for i in range(self.cols):
            if i == c:
                continue
            new.set_col(self.get_col(i), current_col)
            current_col += 1
        return new

    # ROW OPERATIONS END

    # MATRIX DERIVATIVES START

    def get_submatrix(self, row, col):
        return self.delete_col(col).delete_row(row)

    def det(self):        
        return self.__recursive_determinant(self.copy())

    def __recursive_determinant(self, m_matrix):
        dim = m_matrix.get_dim()
        if dim[0] == 1 and dim[1] == 1:
            return m_matrix.get_el(0,0)
        
        row = m_matrix.get_row(0)
        d = 0
        for i in range(dim[1]):
            el = row[i]
            c = (-1)**i
            d += c * el * self.__recursive_determinant(m_matrix.get_submatrix(0, i))
        return d
    
    def get_pivot_element(self, arr):
        for i in range(len(arr)):
            if arr[i] != 0:
                return i
        return -1
    
    def array_reduce_row(self, arr):
        factor = 1
        for e in arr:
            if e != 0:
                factor = e
                break
        new = []
        for e in arr:
            new.append(e / factor)
        return new
    
    def array_multiple(self, n, arr):
        new = []
        for e in arr:
            new.append(e*n)
        return new
    
    def array_add(self, arr1, arr2):
        new = []
        for i in range(len(arr1)):
            new.append(arr1[i] + arr2[i])
        return new
    
    def rref(self):
        newMatrix = self.copy()
        dim = newMatrix.get_dim()
        row_index = 0

        for cnum in range(dim[1]):
            col = newMatrix.get_col(cnum)[row_index:] # only consider rows below current
            piv_row_num = newMatrix.get_pivot_element(col)

            if piv_row_num != -1: #if pivot row exists
                piv_row_num += row_index # get absolute row number, since we only considered rows below current
                if piv_row_num != row_index:
                    newMatrix.switch_row(piv_row_num, row_index)

                piv_row = newMatrix.get_row(piv_row_num)
                reduced_row = newMatrix.array_reduce_row(piv_row)
                newMatrix.set_row(reduced_row, piv_row_num) # Reduce pivot row in place

                piv_row = newMatrix.get_row(piv_row_num) # new reduced pivot row
    
                for r in range(dim[0]):
                    if r == piv_row_num:
                        continue

                    col = newMatrix.get_col(cnum) # update column to current state

                    leading_num = col[r] # leading number in row to be reduced
                    if leading_num != 0:
                        selected_row = newMatrix.get_row(r)
                        reducer = newMatrix.array_multiple(-leading_num, piv_row)

                        reduced_row = newMatrix.array_add(selected_row, reducer)
                        newMatrix.set_row(reduced_row, r)
                row_index += 1
        newMatrix.__clean_zeroes()
        return newMatrix

    def inverse(self):
        if self.rows != self.cols:
            raise Exception("Inverse not defined for non square matrix")
        if self.det() == 0:
            raise Exception("Inverse not defined for singular matrix")
        
        id = Matrix(self.rows, self.cols).set_diag([1]*self.rows, 1)
        new = self.copy()

        aug = Matrix(self.rows, 2*self.cols)
        for r in range(self.rows):
            aug.set_row(new.get_row(r) + id.get_row(r), r)
        
        aug = aug.rref()

        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            new.set_row(aug.get_row(r)[self.cols:], r)
        new.__clean_zeroes()
        return new
    
    def rref_det(self):
        determinant = 1
        mults = []

        newMatrix = self.copy()
        dim = newMatrix.get_dim()
        row_index = 0
        for cnum in range(dim[1]):
            col = newMatrix.get_col(cnum)[row_index:]
            piv_row_num = newMatrix.get_pivot_element(col)

            if piv_row_num != -1:
                piv_row_num += row_index 
                # If there is a valid pivot row, then this shifts it back since get_pivot_element was considering all below the current row index
                if piv_row_num != row_index:
                    newMatrix.switch_row(piv_row_num, row_index)
                    determinant *= -1
                
                for e in newMatrix.get_row(piv_row_num):
                    if e != 0:
                        mults.append(e)
                        break


                newMatrix.set_row(newMatrix.array_reduce_row(newMatrix.get_row(piv_row_num)), piv_row_num) # Turn leading entry to 1

                piv_row = newMatrix.get_row(piv_row_num)
                for r in range(dim[0]):
                    if r == piv_row_num:
                        continue
                    col = newMatrix.get_col(cnum)
                    leading_num = newMatrix.get_el(r, cnum)
                    if leading_num != 0:
                        selected_row = newMatrix.get_row(r)
                        adder = newMatrix.array_multiple(-leading_num, piv_row)
                        new_row = newMatrix.array_add(selected_row, adder)
                        newMatrix.set_row(new_row, r)
                row_index += 1
        
        for mult in mults:
            determinant *= mult
        if newMatrix.get_diag() != [1]*newMatrix.rows:
            determinant = 0
        return determinant 
    
    def pseudoinverse(self):
        t = self.transpose()
        return ((t.matrix_multiply(self)).inverse()).matrix_multiply(t) # (X^T * X)^-1 * X^T

    def rank(self):
        rows = self.rref().get_raw()
        rank = 0
        for row in rows:
            if row != [0]*self.cols:
                rank += 1
        return rank
    
    def nullity(self):
        return self.cols - self.rank()
    
    def ker(self):
        basis = []
        for n in range(self.nullity()):
            basis.append([None]*self.cols)
        free_vars = []
        rref = self.rref()
        current_pivot_row = -1
        for c in range(rref.cols):
            selected_piv_row = rref.get_pivot_element(rref.get_col(c))
            if selected_piv_row <= current_pivot_row:
                free_vars.append(c)
            else:
                current_pivot_row = selected_piv_row
            
        for free_var_num in range(len(free_vars)): # For each free var column
            free_var = free_vars[free_var_num]
            free_col = rref.get_col(free_var)
            for j in range(len(free_col)): # Go down it
                row = rref.get_row(j)
                row_variable = rref.get_pivot_element(row) # Look at what variable the row represents
                basis[free_var_num][row_variable] = -rref.get_el(j, free_var) # Add the negative of the selected el in the basis
        for i in range(len(free_vars)):
            basis[i][free_vars[i]] = 1 # Set x_n = x_n for free x_n 
        for i in range(len(basis)):
            for j in range(len(basis[i])):
                if basis[i][j] is None:
                    basis[i][j] = 0
        return basis

    def colspace(self):
        basis = []
        rref = self.rref()
        for i in range(rref.cols):
            basis.append(rref.get_col(i))
        return basis
    
    def is_in_span(self, vector, span):
        coefficient_cols = len(span)
        m = Matrix(len(span[0]), coefficient_cols+1)
        for i in range(coefficient_cols):
            m.set_col(span[i],i)
        m.set_col(vector, coefficient_cols) #last

        newMatrix = m

        # TRANSPLANTED CODE FROM RREF, just changed to not consider augmented column
        dim = newMatrix.get_dim()
        row_index = 0
        for cnum in range(dim[1])[:-1]: 
            col = newMatrix.get_col(cnum)[row_index:] # only consider rows below current
            piv_row_num = newMatrix.get_pivot_element(col)

            if piv_row_num != -1: #if pivot row exists
                piv_row_num += row_index # get absolute row number, since we only considered rows below current
                if piv_row_num != row_index:
                    newMatrix.switch_row(piv_row_num, row_index)

                piv_row = newMatrix.get_row(piv_row_num)
                reduced_row = newMatrix.array_reduce_row(piv_row)
                newMatrix.set_row(reduced_row, piv_row_num) # Reduce pivot row in place

                piv_row = newMatrix.get_row(piv_row_num) # new reduced pivot row
    
                for r in range(dim[0]):
                    if r == piv_row_num:
                        continue

                    col = newMatrix.get_col(cnum) # update column to current state

                    leading_num = col[r] # leading number in row to be reduced
                    if leading_num != 0:
                        selected_row = newMatrix.get_row(r)
                        reducer = newMatrix.array_multiple(-leading_num, piv_row)

                        reduced_row = newMatrix.array_add(selected_row, reducer)
                        newMatrix.set_row(reduced_row, r)
                row_index += 1
        
        rref = newMatrix

        for r in range(rref.get_dim()[0]):
            row = rref.get_row(r)
            if row[:-1] == [0]*len(row[:-1]) and row[-1] != 0: # Inconsistent row
                return False
        return True


    # MATRIX DERIVATIVES END
        
        
    # UTIL

    def __clean_zeroes(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.get_el(r,c) < 0.0000001 and self.get_el(r,c) > -0.0000001:
                    self.set_el(0.0, r,c)

    def copy(self):
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                new.set_el(self.get_el(r, c), r, c)
        return new
    
    def display(self):
        print("\n")
        for r in range(self.rows):
            for c in range(self.cols):
                el = self.get_el(r, c)
                print(el, end= "    ")
            print("\n")
        print("\n")
        print("-")
        return self