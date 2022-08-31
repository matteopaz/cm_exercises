class Matrix:


    def __init__(self, rows, cols, start_elem=0):
        self.m = []
        self.rows = rows
        self.cols = cols
        for i in range(self.rows):
            self.m.append([start_elem] *self.cols)

    def __copy(self, arr):
        new = []
        for row in self.m:
            new.append(row)
        return new        
    
    # GETTERS START
    def e(self, r, c):
        return self.m[r - 1][c - 1]

    def r(self, n):
        if not n:
            raise Exception("Rows start from 1")
        return self.m[n - 1][::1]
    
    def c(self, n):
        if not n:
            raise Exception("Cols start from 1")
        col = []
        for row in self.m:
            col.append(row[n - 1])
        return col

    def d(self, n):
        if self.rows != self.cols:
            raise Exception("Diagonal not defined for rect matrix") 
        dim = self.rows
        diag = []
        if n == 1:
            for i in range(dim):
                diag.append(self.m[i][i])
        if n == 2:
            for i in range(dim):
                diag.append(self.m[dim - 1 -i][i])
        return diag
    
    def getdim(self):
        return [int(self.rows), int(self.cols)]
    
    def all(self):
        return self.__copy(self.m)
    
    # GETTERS END
    # SETTERS START

    def setel(self, val, r, c):
        self.m[r - 1][c - 1] = val
        return self

    
    def setr(self, val, r):
        if not isinstance(val, list):
            raise Exception("Use a list when setting rows/cols")
        if len(val) != self.cols:
            raise Exception("Set list length not equal to matrix dimension")
        self.m[r - 1] = val
        return self

    def setc(self, val, c):
        if not isinstance(val, list):
            raise Exception("Use a list when setting rows/cols")
        if len(val) != self.rows:
            raise Exception("Set list length not equal to matrix dimension")

        for r in range(len(self.m)):
            self.m[r][c - 1] = val[r]
        return self
        
    def setd(self, val, d):
        if self.rows != self.cols:
            raise Exception("Diagonal not defined for rect matrix")

        dim = self.rows

        if not isinstance(val, list):
            raise Exception("Use a list when setting rows/cols")
        if len(val) != dim:
            raise Exception("Set list length not equal to matrix dimension")

        if d == 1:
            for i in range(dim):
                self.m[i][i] = val[i]
        if d == 2:
            for i in range(dim):
                self.m[dim - 1 -i][i] = val[i]
        return self
    
    def fill(self, val):
        for i in range(self.rows):
            for j in range(self.cols):
                self.setel(val, i+1, j+1)
        return self

    def setm(self, m):
        if len(m) != self.rows or len(m[0]) != self.cols:
            raise Exception("Matrix dimension mismatch")
        for i in range(self.rows):
            for j in range(self.cols):
                self.setel(m[i][j], i+1, j+1)
        return self

    # SETTERS OVER

    # SCALAR OPERATIONS 

    def scalar_multiply(self, n):
        new = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.e(i + 1, j + 1) * n
                new.setel(val, i + 1, j + 1)
        return new

    # SCALAR OPERATIONS END

    # MATRIX ON MATRIX OPERATIONS START

    def add(self, adder):
        if not isinstance(adder, Matrix):
            raise Exception("Please use matrix of same dimension")
        new = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.e(i + 1, j + 1) + adder.e(i + 1, j + 1)
                new.setel(val, i + 1, j + 1)
        return new
    
    def subtract(self, m):
        return self.add(m.scalar_multiply(-1))

    def matrix_multiply(self, mult):
        if not isinstance(mult, Matrix):
            raise Exception("Cannot multiply matrix by non matrix type, try scalar_multiply")

        multdim = mult.getdim()
        if self.cols != multdim[0]:
            raise Exception("Matrix multiplication incompatible")

        new = Matrix(self.rows, multdim[1], 0)
        for rownum in range(self.rows):
            row = self.r(rownum + 1)
            for colnum in range(multdim[1]):
                multcol = mult.c(colnum + 1)
                val = 0
                for i in range(self.cols):
                    val += row[i] * multcol[i]
                new.setel(val, rownum+1, colnum+1)
        return new
    
    # MATRIX ON MATRIX OPERATIONS END


    # ROW OPERATIONS START

    def transpose(self):
        if self.rows != self.cols:
            raise Exception("Diagonal not defined for rect matrix")
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                new.setel(self.e(r+1,c+1), c+1, r+1)
        return new
    
    def switch_row(self, one, two):
        prev = self.r(one)
        next = self.r(two)
        self.setr(next, one)
        self.setr(prev, two)
        return self
    
    def switch_col(self, one, two):
        prev = self.c(one)
        next = self.c(two)
        self.setc(next, one)
        self.setc(prev, two)
        return self    
    
    def delete_row(self, r):
        new = Matrix(self.rows - 1, self.cols)
        current_row = 1
        for i in range(self.rows):
            if i + 1 == r:
                continue
            new.setr(self.r(i+1), current_row)
            current_row += 1
        return new        

    def delete_col(self, c):
        new = Matrix(self.rows, self.cols - 1)
        current_col = 1
        for i in range(self.cols):
            if i + 1 == c:
                continue
            new.setc(self.c(i+1), current_col)
            current_col += 1
        return new

    # ROW OPERATIONS END

    # MATRIX DERIVATIVES START

    def submatrix(self, row, col):
        return self.delete_col(col).delete_row(row)

    def det(self):        
        def inner(m_matrix):
            dim = m_matrix.getdim()
            if dim[0] == 1 and dim[1] == 1:
                return m_matrix.e(1,1)
            
            row = m_matrix.r(1)
            d = 0
            for i in range(dim[1]):
                el = row[i]
                c = (-1)**i
                d += c * el * inner(m_matrix.submatrix(1, i+1))
            return d
        return inner(self.copy())
        

    # MATRIX DERIVATIVES END
    # UTIL

    def copy(self):
        new = Matrix(self.rows, self.cols)
        for rownum in range(self.rows):
            for colnum in range(self.cols):
                new.setel(self.e(rownum+1, colnum+1), rownum+1, colnum+1)
        return new
    
    def display(self):
        print("\n")
        for row in self.m:
            for el in row:

                print(el, end="    ")
            print("\n")
        print("\n")
        print("-")
        return self.all()
    

mone = Matrix(3,3)

