# class MultiPolynomial:
#     def __init__(self, order, coeffs):
#         self.order = order
#         self.coeffs = coeffs

class Polynomial:
    def __init__(self, order, coeffs):
        if len(coeffs) != order:
            raise ValueError("Invalid number of coefficients")
        self.order = order
        self.coeffs = coeffs
    

    def eval(self, x):
        val = 0
        ascending_coeffs = self.get_coefficients()[::-1]
        for deg in range(self.order):
            val += x**deg * ascending_coeffs[deg]
            print(f"deg: {deg}, co: {ascending_coeffs[deg]},  val: {val}")
        return val

    def get_coefficients(self):
        return self.coeffs
    
    def get_order(self):
        return self.order

    def get_derivative(self, nth, __poly=None):
        if not __poly:
            __poly = self

        if nth == 0:
            return __poly
        
        if __poly.get_order() == 1:
            return Polynomial(1, [0])

        ascending_coeffs = __poly.get_coefficients()[::-1]
        for deg in range(__poly.get_order()):
            ascending_coeffs[deg] *= deg
        coeffs = ascending_coeffs[::-1]
        new = Polynomial(__poly.get_order() - 1, coeffs[:-1])
        return self.get_derivative(nth - 1, new)
    
    def add(self, poly):
        if poly.get_order() > self.get_order():
            return poly.add(self)

        self_coeffs = self.get_coefficients()
        poly_coeffs = poly.get_coefficients()
        for deg in range(poly.get_order()):
            self_coeffs[deg] += poly_coeffs[deg]
        return Polynomial(self.get_order(), self_coeffs)
    
    def multiply(self, poly):
        self_coeffs = self.get_coefficients()
        poly_coeffs = poly.get_coefficients()
        self_order = self.get_order()
        poly_order = poly.get_order()

        coeffs = [0] * (self_order + poly_order - 1)
        for deg in range(self.get_order()):
            for deg2 in range(poly.get_order()):
                coeffs[deg + deg2] += self_coeffs[deg] * poly_coeffs[deg2]
        return Polynomial(self.get_order() + poly.get_order() - 1, coeffs)
    
    def __recursive_newton(self, x, acc):
        tan_root = x - self.eval(x) / self.get_derivative(1).eval(x)
        
        if x - tan_root < 10**(-1*acc):
            roundable = tan_root * 10**(acc)
            rounded = round(roundable) / 10**(acc)
            return rounded

        return self.__recursive_newton(tan_root, acc)

    def roots(self):
        return self.__recursive_newton(1, 5)
        

    def __str__(self):
        coeffs = self.get_coefficients()
        order = self.get_order()

        s = ""
        for i in range(order):
            deg = order - i - 1
            if coeffs[i] == 0:
                if deg == 0:
                    s += "  0"
                continue
            if deg == 0:
                s += "  " + str(coeffs[i])
            elif deg == 1:
                s += "  {}x".format(coeffs[i])
            else:
                s += "  {}x^{}".format(coeffs[i], deg)

        return s

    def display(self):
        print(self.__str__())
        return self

p = Polynomial(3, [1,-2,1])
n = Polynomial(3, [1,2,1])
d = p.multiply(n).get_derivative(1).display()
print(d.eval(3))
