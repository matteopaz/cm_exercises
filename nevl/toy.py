import numpy as np
from helpers import *
import matplotlib.pyplot as plt

t = lambda x: np.tanh(x)

data = [
  (0.0, 1.0), (0.04, 0.81), (0.08, 0.52), (0.12, 0.2), (0.17, -0.12),
  (0.21, -0.38), (0.25, -0.54), (0.29, -0.58), (0.33, -0.51), (0.38, -0.34),
  (0.42, -0.1), (0.46, 0.16), (0.5, 0.39), (0.54, 0.55), (0.58, 0.61),
  (0.62, 0.55), (0.67, 0.38), (0.71, 0.12), (0.75, -0.19), (0.79, -0.51),
  (0.83, -0.77), (0.88, -0.95), (0.92, -1.0), (0.96, -0.91), (1.0, -0.7)
]

def initWB(shape):
    W = []
    B = []
    for i in range(len(shape) - 1):
        W.append(np.random.rand(shape[i+1], shape[i]))
        B.append(np.random.rand(shape[i+1], 1))
    return W, B


wts = [initWB([1, 16, 4, 2, 1]) for i in range(15)]

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

class ann(fc):
    def __init__(self, shape):
        weights, biases = initWB(shape)
        super().__init__(weights, biases)

def MSELoss(model, data):
    total = 0
    for pt in data:
        inp, label = pt
        total += (model(np.array([[inp]])) - label)**2
    return total / len(data)

def N():
    return np.random.normal()


EPOCHS = 1000
a0 = 0.5
kidmult = 1
population = 15
top = 10

numweights = 0
for mtx in wts[0][0]:
    numweights += mtx.size
for mtx in wts[0][1]:
    numweights += mtx.size




papas = [(fc(wts[i][0], wts[i][1]), a0) for i in range(15)]
firstgen = np.copy(papas)

def mutate(wts, lr):
    new = []
    for mtx in wts:
        newmtx = np.copy(mtx)
        for e in newmtx:
            e += lr * N()
        new.append(newmtx)
    return new

avgloss = []

for epoch in range(EPOCHS):

    kiddos = []
    for papa in papas:
        lr = papa[1]
        newlr = lr * math.exp(N() / math.sqrt(2 * math.sqrt(numweights)))
        wts = mutate(papa[0].w, newlr)
        bs = mutate(papa[0].b, newlr)
        kiddos.append((fc(wts, bs),newlr))
    
    all = papas + kiddos
    scores = [0 for i in range(len(all))]
    genloss = 0
    for i in range(len(all)):
        genloss += MSELoss(all[i][0].forward, data)
        scores[i] = MSELoss(all[i][0].forward, data)
    
    avgloss.append(genloss.item() / len(all))

    papas = [x for _, x in sorted(zip(scores, all))][:16] # best 15

    print("Epoch: ", epoch, "Loss: ", round(genloss.item()*100)/100)

# x = range(EPOCHS)
# y = avgloss



# plt.plot(x, y)


for pt in data:
    plt.plot(pt[0], pt[1], "r.")
winner = papas[-1][0]

x = []
y = []
for i in range(0,500):
    inp = i /500
    x.append(inp)
    y.append(winner.forward(np.array([[inp]])).item())

plt.plot(x, y)
plt.show()





