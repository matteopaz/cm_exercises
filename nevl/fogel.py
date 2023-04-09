import random
import matplotlib.pyplot as plt
import numpy as np
import sys
from tictactoe import TicTacToe, Player, random_strategy, perfect, almost_perfect
from nn import ANN, fc
from helpers import save

def play(model, strategy):
    p1 = Player(model, 1, nn=True)
    p2 = Player(strategy, -1)
    game = TicTacToe(p1, p2)
    return game.run(False)

def N():
    return np.random.normal(0, 0.05**2)

def mutate(wts):
    newwts = []
    newb = []
    for mtx in wts[0]:
        newmtx = np.copy(mtx)
        for e in newmtx:
            e += N()
        newwts.append(newmtx)

    for mtx in wts[1]:
        newmtx = np.copy(mtx)
        for e in newmtx:
            e += N()
        newb.append(newmtx)
    
    if np.random.randint(0, 2):
        if np.random.randint(0, 2):
            newwts[1] = newwts[1][:, :-1] # Remove a column aka remove a node from hidden layer
            newwts[0] = newwts[0][:-1, :] # remove a row
            newb[0] = newb[0][:-1, :] # remove a row
        else:
            newwts[1] = np.concatenate((newwts[1], np.random.rand(*(newwts[1].shape[0], 1))), axis=1) # Add a column
            newwts[0] = np.concatenate((newwts[0], np.random.rand(*(1, newwts[0].shape[1]))), axis=0) # Add a row
            newb[0] = np.concatenate((newb[0], np.random.rand(*(1, 1))), axis=0) # Add a row
    return newwts, newb

startpop = 50
kidsper = 1

papas = [[ANN([9, np.random.randint(1, 11), 9], rad=0.5), 0] for i in range(startpop)] # network, score

losses = []

for i in range(200):
    for papa in papas:
        papa[1] = 0
        for j in range(32):
            win = play(papa[0], perfect)
            if win == 1:
                papa[1] += 1
            elif win == -1:
                papa[1] -= 1
            else:
                papa[1] -= 1

    # select top 25 parents
    papas.sort(key=lambda x: x[1], reverse=True)
    papas = papas[:(startpop//kidsper+1)]

    # log best score
    print("Epoch: ", i, "Best Score: ", papas[0][1])
    losses.append(papas[0][1])
    
    for j in range(len(papas)):
        papa = papas[j]
        for k in range(kidsper):
            papas.append([fc(*mutate((papa[0].w, papa[0].b))), 0])


plt.plot(losses)
plt.show()
save((papas[0][0].w, papas[0][0].b), "bestmodel.pkl")
    
