class Matrix:


    def __init__(self, rows, cols, start_elem=0):
        self.raw = []
        self.rows = rows
        self.cols = cols
        for i in range(self.rows):
            self.raw.append([start_elem] *self.cols)

    def __copy(self, arr):
        new = []
        for row in self.raw:
            new.append(row)
        return new        
    
    # GETTERS START
    def el(self, r, c):
        return self.raw[r][c]

    def r(self, n):
        new = []
        for c in range(self.cols):
            new.append(self.el(n, c))
        return new
    
    def c(self, n):
        new = []
        for r in range(self.rows):
            new.append(self.el(r, n))
        return new

    def d(self, n):
        if self.rows != self.cols:
            raise Exception("Diagonal not defined for rect matrix") 
        dim = self.rows
        diag = []
        if n == 1:
            for i in range(dim):
                diag.append(self.el(i,i))
        if n == 2:
            for i in range(dim):
                diag.append(self.el(dim - 1 - i, i))
        return diag
    
    def getdim(self):
        return [int(self.rows), int(self.cols)]
    
    def all(self):
        new = []
        for r in range(self.rows):
            new.append(self.r(r))
        return new
    
    # GETTERS END
    # SETTERS START

    def setel(self, val, r, c):
        self.raw[r][c] = val
        return self

    
    def setr(self, val, r):
        if not isinstance(val, list):
            raise Exception("Use a list when setting rows/cols")
        if len(val) != self.cols:
            raise Exception("Set list length not equal to matrix dimension")
        self.raw[r] = val
        return self

    def setc(self, val, c):
        if not isinstance(val, list):
            raise Exception("Use a list when setting rows/cols")
        if len(val) != self.rows:
            raise Exception("Set list length not equal to matrix dimension")

        for r in range(len(self.raw)):
            self.raw[r][c] = val[r]
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
                self.raw[i][i] = val[i]
        if d == 2:
            for i in range(dim):
                self.raw[dim - 1 -i][i] = val[i]
        return self
    
    def fill(self, val):
        for r in range(self.rows):
            for c in range(self.cols):
                self.setel(val, r, c)
        return self

    def setm(self, m):
        if len(m) != self.rows or len(m[0]) != self.cols:
            raise Exception("Matrix dimension mismatch")
        for r in range(self.rows):
            for c in range(self.cols):
                self.setel(m[r][c], r, c)
        return self

    # SETTERS OVER

    # SCALAR OPERATIONS 

    def scalar_multiply(self, n):
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                val = self.el(r, c) * n
                new.setel(val, i, j)
        return new

    # SCALAR OPERATIONS END

    # MATRIX ON MATRIX OPERATIONS START

    def add(self, adder):
        if not isinstance(adder, Matrix):
            raise Exception("Please use matrix of same dimension")
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                val = self.el(r, c) + adder.el(r, c)
                new.setel(val, r, c)
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
        for r in range(self.rows):
            row = self.r(r)
            for c in range(multdim[1]):
                multcol = mult.c(c)
                val = 0
                for el in range(len(row)):
                    val += row[el] * multcol[el]
                new.setel(val, r, c)
        return new
    
    # MATRIX ON MATRIX OPERATIONS END


    # ROW OPERATIONS START

    def transpose(self):
        if self.rows != self.cols:
            raise Exception("Diagonal not defined for rect matrix")
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                new.setel(self.el(r,c), c, r)
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
        current_row = 0
        for i in range(self.rows):
            if i == r:
                continue
            new.setr(self.r(i), current_row)
            current_row += 1
        return new        

    def delete_col(self, c):
        new = Matrix(self.rows, self.cols - 1)
        current_col = 0
        for i in range(self.cols):
            if i == c:
                continue
            new.setc(self.c(i), current_col)
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
                return m_matrix.el(0,0)
            
            row = m_matrix.r(1)
            d = 0
            for i in range(dim[1]):
                el = row[i]
                c = (-1)**i
                d += c * el * inner(m_matrix.submatrix(0, i))
            return d
        return inner(self.copy())
        

    # MATRIX DERIVATIVES END
    # UTIL

    def copy(self):
        new = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                new.setel(self.el(r, c), r, c)
        return new
    
    def display(self):
        print("\n")
        for r in range(self.rows):
            for c in range(self.cols):
                el = self.el(r, c)
                print(el, end="    ")
            print("\n")
        print("\n")
        print("-")
        return self.all()
    

mone = Matrix(3,3)

