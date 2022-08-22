import random
import math

def draw_rand(dist):
    cumulative = []

    for i in range(len(dist)):
        prev = 0
        if i > 0:
            prev = cumulative[i - 1]
        current = dist[i]

        cumulative.append(prev + current)

    rand = random.random()
    for p in cumulative:
        if rand <= p:
            return cumulative.index(p)

distribution_one = [0.1,0.2,0.3,0.4]

result = [0]*len(distribution_one)
test_count = 100000


for i in range(test_count):
    result[draw_rand(distribution_one)] += 1

for i in range(len(result)):
    result[i] = result[i] / test_count

print(result)