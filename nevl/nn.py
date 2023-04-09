from helpers import nextlayer
import numpy as np


t = lambda x: np.tanh(x)

def initWB(shape, rad=1):
    W = []
    B = []
    for i in range(len(shape) - 1):
        W.append(np.random.rand(shape[i+1], shape[i]) * rad)
        B.append(np.random.rand(shape[i+1], 1) * rad)
    return W, B

class fc:
    def __init__(self, weights=None, biases=None):
        if weights:
            self.w = weights
        if biases:
            self.b = biases
        self.layers = len(self.w)
    
    def forward(self, inp):
        s = [inp]
        h = [inp]
        for i in range(self.layers):
            s.append(nextlayer(self.w[i], h[i], self.b[i]))
            h.append(t(s[i+1]))
        return h[-1]
    
    def __call__(self, inp):
        return self.forward(inp)

class ANN(fc):
    def __init__(self, shape, rad=1):
        weights, biases = initWB(shape, rad)
        self.shape = shape
        super().__init__(weights, biases)
    