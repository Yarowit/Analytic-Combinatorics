import matplotlib.pyplot as plt
import numpy as np

sigma = [0]
p = [1] # p0 = 1 p1 = 1

maxn = 100

for n in range(1,maxn):
    sigma.append(n)
    for i in range(1,n):
        if n%i == 0:
            sigma[n] += i 

        
    # i = 1
    # while i < isqrt:
    #     if n%i == 0:
    #         sigma[n] += i + n//i
    #     i += 1

    p.append(sum([sigma[j]*p[n-j] for j in range(1,n+1)])  // n)

def f(n): # ~ 13^x / x
    return 1/(4*n*(3**0.5))*np.exp(np.pi*(2*n/3)**0.5)

xax = range(2,maxn)
factorial = [1]
for i in range(1,maxn):
    factorial.append(factorial[i-1]*i)

plt.plot(
    xax,
    [p[i]/f(i) for i in xax],
    label="p_n"
)


plt.legend()
plt.show()

# złożoność: O(n + sqrt(n)) = O(n)

print(sigma)
print(p)