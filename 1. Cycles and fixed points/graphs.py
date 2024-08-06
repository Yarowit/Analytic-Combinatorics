import matplotlib.pyplot as plt
import numpy as np
from os import listdir 
# DANE

filename = "Random_aaaCount"

def plotResults(filename, isExponential):
    plt.figure()
    file = open("./data/"+filename,"r")

    vals = [(float)(line[:-1]) for line in file]
    # print(vals)
    x = list(range(4,len(vals)+4)) # pierwsze 4 to zera

    a=0
    b=0
    
    if(isExponential == True):
        logvals = np.log(vals)
        a, b = np.polyfit(x, logvals, 1)
        fity = [np.exp(b) * np.exp(a*i) for i in x]
        plt.plot(x, fity, label = "fit exp")
        plt.yscale("log")
    else:
        a, b = np.polyfit(x, vals, 1)
        fity = [i*a+b for i in x]
        plt.plot(x,fity,label='fit')

    plt.plot(x, vals, label = filename)


    print(a,b)

    plt.legend()
    # plt.show()
    if isExponential:
        plt.title((str)(np.exp(a))+" ^ x + "+(str)(np.exp(b)))
        plt.savefig("graphs/E_"+filename+".png")
    else:
        plt.title((str)(a)+" * x + "+(str)(b))
        plt.savefig("graphs/L_"+filename+".png")

for file in listdir("./data"):
    plotResults(file,False)
    plotResults(file,True)
    
#       aaa
# plotResults("aaa",True)
# y ≈ e^(-2.07248) * e^(0.73946*x)
# Hipoteza:
# y = 2^n / e^2
# wraz z odcinaniem wartości początkowych baza potęgi dąży do 2,
# zaś mianownik się zmniejsza, więc e^2 może być zawyżone

#       abb
# plotResults("abb",True)
# y ≈ e^(-1.69305) * e^(0.73388*x)
# y ≈ e^(-0.86102) * e^(0.69898*x) ~ po odjęciu pierwszych 14 punktów
# Hipoteza:
# y = 2^n / 2
# wraz z odcinaniem wartości początkowych baza potęgi dąży do 2,
# zaś mianownik zbliża się do 2

#       Średnia liczba aaa
# plotResults("aaaCount",False)
# y ≈ 0.12545 * x - 0.38462
# Hipoteza: ???
# Dziwne współczynniki, ale zależność jest czysto liniowa i bardzo dokładna od samge początku