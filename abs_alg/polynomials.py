class Polynomial:
    def __init__(self, order, coeffs):
        self.order = order
        self.coeffs = coeffs
        self.ascending_coeffs = coeffs[::-1]
    

    def eval(self, x):
        val = 0
        for deg in range(self.order):
            val += x**deg + self.ascending_coeffs[deg]
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

        ascending_coeffs = __poly.get_coefficients()[::-1]
        for deg in range(__poly.get_order()):
            ascending_coeffs[deg] *= deg
        coeffs = ascending_coeffs[::-1]
        new = Polynomial(__poly.get_order() - 1, coeffs)
