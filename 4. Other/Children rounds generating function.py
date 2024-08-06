# Wolfram:
# Series[[//math:1/(1-x)^x//], {[//math:x//], [//math:0//], [//math:100//]}]
# N[] - przybliża
# Zbiega do 1, asymptotyka ~ n!

import matplotlib.pyplot as plt
res = [
    1,
    0,
    1,
    1/2,
    5/6,
    3/4,
    33/40,
    5/6,
    2159/2520,
    209/240,
    8909/10080,
    601/672,
    18028763/19958400,
    3673/4032
]
def f(n):
    return n*f(n-1) if n != 0 else 1
plt.plot(
    [i for i in range(len(res))],
    res
)
    # [f(i)*res[i] for i in range(len(res))]
	
plt.show()