import math
def b(n):
    if n == 0:
        return 1
    return n**2 * b(n-1) + 1

def B(n):
    return math.factorial(n)**2 * ( sum([1/math.factorial(k)**2 for k in range(n+1)]))

def linearB(n):
    s = 0
    for i in range(n+1):
        s = (s+1)*i*i
    return s + 1
    # to jest to samo co wzór rekurencyjny...


for i in range(10):
    print(b(i),B(i), linearB(i))


def lim(n):
    return sum([1/math.factorial(k)**2 for k in range(n+1)])

import matplotlib.pyplot as plt
xax = [i for i in range(1,10)]
plt.plot(
    xax,
    [lim(x) for x in xax],
    label="s(n)"
)
plt.legend()
plt.show()