import numpy as np
from random import *
import matplotlib.pyplot as plt

def randomTup(n, elems, prob):
    return choices(elems,prob,k=n)

# print(randomTup(5,['a','b'],[2,1]))

n = 100
repeats = 100
xax = []
yax = []
for p in range (100):
    aaaAverage = 0
    for k in range(repeats):
        x = randomTup(n, ['a','b'], [p,100-p])
        aaaCount = 0
        aCount = 0
        for i in range(len(x)-3):
            if x[i] == 'a':
                aCount += 1
            else:
                aCount = 0

            if aCount >= 3:
                aaaCount += 1
        aaaAverage += aaaCount / repeats
        
    xax.append(p)
    yax.append(aaaAverage)
    
plt.plot(xax,yax)
plt.show()

    