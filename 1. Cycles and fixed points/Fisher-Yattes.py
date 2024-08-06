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

# Zwraca tablicę z cyklami arr
def divideIntoCycles(arr):
    order = list(range(len(arr)))
    cycleArr = []
    while(len(order) > 0):
        start = arr[order[0]]
        order.remove(start)
        next = arr[start]
        cycle = [start]
        while next != start:
            cycle.append(next)
            order.remove(next)
            next = arr[next]
        cycleArr.append(cycle)
    return cycleArr

# Zwraca liczbę cykli arr
def numberOfCycles(arr):
    order = list(range(len(arr)))
    n = 0
    while len(order) > 0:
        start = arr[order[0]]

        order.remove(start)
        next = arr[start]
        while next != start:
            order.remove(next)
            next = arr[next]
        n = n + 1
    return n

# Zwraca średnią liczbę cykli permutacji długości n
def averageCycleNumber(n):
	sum = 0
	for i in range(2000):
		perm = FisherYatesShuffle(list(range(n)))
		sum = sum + numberOfCycles(perm)
	return sum / 2000.0
# Zwraca n-tą liczbę harmoniczną
def H(n):
	h = 0
	for i in range(1, n + 1):
		h = h + 1.0 / i
	return h

def fixedPointCount(arr):
	count = 0
	for i in range(len(arr)):
		if i+1 == arr[i]:
			count += 1
	return count

# Rysuje wykresy powyższych funkcji dla n od 1 do 100
def cyclePlot():
	plt.figure()
	order = list(range(1, 101))
	
	avTab = []
	for i in range(1, 101):
		avTab.append(averageCycleNumber(i))
	plt.plot(order, avTab, label = "Averages")
	
	harTab = []
	for i in range(1, 101):
		harTab.append(H(i))
	plt.plot(order, harTab, label = "Harmonics")
	
	
	plt.legend()
	# plt.savefig("plt.png")
	plt.show()
# 0.624218226822682 0.30767454545455103
# plot(int(input("Mode: "))) # 1, 2, 3 or 4

def PunktyStale():
	tab0 = []
	tab1 = []
	tab2 = []
	intervals = range(100,1000,100)
	repeats = 1000
	for n in intervals:
		av0 = 0
		av1 = 0
		av2 = 0
		for k in range(repeats):
			arr = list(range(1,n))
			FisherYatesShuffle(arr)
			fp = fixedPointCount(arr)
			av0 += (fp == 0)
			av1 += (fp == 1)
			av2 += (fp == 2)
		tab0.append(av0)
		tab1.append(av1)
		tab2.append(av2)
	plt.figure()
	plt.plot(intervals, tab0, label = "Zero punktów stałych")
	plt.plot(intervals, [repeats/np.e]*len(intervals), label = "1/e")
	a, b = np.polyfit(intervals, tab0, 1)
	plt.plot(intervals,intervals*a+b,label='0')
	plt.legend()
	plt.show()
	plt.figure()
	plt.plot(intervals, tab1, label = "Jeden punkt stały")
	plt.plot(intervals, [repeats/(np.e)]*len(intervals), label = "1/e")
	a, b = np.polyfit(intervals, tab1, 1)
	plt.plot(intervals,intervals*a+b,label='1')
	plt.legend()
	plt.show()
	plt.figure()
	plt.plot(intervals, tab2, label = "Dwa punkty stałe")
	plt.plot(intervals, [repeats/(2*np.e)]*len(intervals), label = "1/2e")
	a, b = np.polyfit(intervals, tab2, 1)
	plt.plot(intervals,intervals*a+b,label='2')
	plt.legend()
	plt.show()




		

# order = list(range(1, 10))
# swap(order,2,3)
# ne = FisherYatesShuffle(order)
# print(order)
# print(ne)
# print(fixedPointCount(order))

cyclePlot()
PunktyStale()