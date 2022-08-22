import random
import matplotlib as mpl
import matplotlib.pyplot as plt

sampleSize = 1000

def sim_probability(heads, flips):
    success = 0

    for i in range(sampleSize):
        trial_heads = 0
        for i in range(flips):
            r = random.random()
            if r > 0.5:
                trial_heads +=1
        if trial_heads == heads:
            success += 1
     
            
    return success / sampleSize

fig, ax = plt.subplots()

flips = 50
x = range(flips)
y = []
for v in x:
    y.append(sim_probability(v, flips))

print(y)
ax.plot(x,y)
plt.savefig(fname="./test.png", format="png")