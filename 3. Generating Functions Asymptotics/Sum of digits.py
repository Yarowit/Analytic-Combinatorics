import numpy as np
import matplotlib.pyplot as plt

def sd(n):
    sum = 0
    while n > 0:
        sum += n%2
        n = n//2
    return sum

def s(n):
    sum = 0
    for i in range(1,n+1):
        sum += sd(i)
    return sum

def a(n):
    return n/2*np.log2(n)

def plot():
    xax = [i for i in range(2,1025)]
    plt.plot(
        xax,
        [s(x) for x in xax],
        label="s(n)"
    )
    plt.legend()
    plt.show()
    plt.plot(
        xax,
        [s(x)/x for x in xax],
        label="s(n)/n"
    )
    plt.legend()
    plt.show()
    plt.plot(
        xax,
        [s(x)/a(x) for x in xax],
        label="s(n) / nlog(n)/2"
    )
    plt.legend()
    plt.show()
    plt.plot(
        xax,
        [s(x)-a(x) for x in xax],
        label="s(n) - nlog(n)/2"
    )
    plt.legend()
    plt.show()

plot()