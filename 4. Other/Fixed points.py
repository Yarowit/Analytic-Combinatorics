import random as r
import numpy as np
import matplotlib.pyplot as plt

def swap (arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

# Zwraca losową permutację arr
def FisherYatesShuffle (arr):
    for i in range(len(arr) - 1):
        j = r.randint(i, len(arr) - 1)
        arr = swap(arr, i, j)
    return arr


def fixedPointCount(arr):
	count = 0
	for i in range(len(arr)):
		if i+1 == arr[i]:
			count += 1
	return count

def PunktyStale():
	xax = []
	yax = []
	
	repeats = 1000
	for n in range(2,101):
		av = 0
		for k in range(repeats):
			arr = list(range(1,n))
			FisherYatesShuffle(arr)
			av += fixedPointCount(arr)
		av /= repeats

		xax.append(n)
		yax.append(av)
	plt.figure()
	plt.plot(xax, yax, label = "Średnia liczba punktów stałych")
	
	plt.legend()
	plt.show()


PunktyStale()

# Hipoteza: 1
# Dowód:
# Liczba punktów stałych: suma X_i, gdzie i-ty
# Prawdopodobieństwo tego, że punkt wyląduje na swoim miejscu to 1/n