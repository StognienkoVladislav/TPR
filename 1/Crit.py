

import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt
from pandas import DataFrame, Series


#Слейтер
def Sl(PX):

    for xi in PX:
        if not xi[2]:
            continue

        for xj in PX:
            if xi == xj or not xj[2]:
                continue

            if xj[0] > xj[0] and xi[1] > xj[1]:
                xj[2] = 0

            else:
                if xj[0] > xi[0] and xj[1] > xi[1]:
                    xi[2] = 0
                    break

    return PX

#Парето
def Pareto(PX):

    for xi in PX:
        if not xi[2]:
            continue

        for xj in PX:
            if xi == xj or not xj[2]:
                continue

            if xi[0] >= xj[0] and xi[1] >= xj[1]:
                xj[2] = 0

            else:
                if xj[0] >= xi[0] and xj[1] >= xi[1]:
                    xi[2] = 0
                    break

    return PX

def display(SPX, PPX, X):

    plt.figure()

    SPX = [[x[0], x[1]] for x in SPX if x[2]]
    SPX.sort(key=lambda x: x[1])

    plt.subplot(2, 1, 2)
    plt.plot([x[0] for x in X], [x[1] for x in X], 'bo')
    plt.plot([x[0] for x in SPX], [x[1] for x in SPX], 'ro')
    plt.plot([x[0] for x in SPX], [x[1] for x in SPX], 'r--')
    plt.title("Slayter")
    plt.axis([-1, 10, -1, 10])


    PPX = [[x[0], x[1]] for x in PPX if x[2]]
    PPX.sort(key = lambda x : x[1])



    plt.subplot(2, 1, 1)
    plt.plot([x[0] for x in X], [x[1] for x in X], 'bo')
    plt.plot([x[0] for x in PPX], [x[1] for x in PPX], 'ro')
    plt.plot([x[0] for x in PPX], [x[1] for x in PPX], 'r--')
    plt.title("Pareto")
    plt.axis([-1, 10, -1, 10])

    plt.show()



if __name__ == '__main__':
    dataFrame = pd.read_json('1/example.json')

    print(dataFrame)

    PPX = [[dataFrame['example1']['q1'][z], [dataFrame['example1']['q2'][z]], 1] for z in range(20)]
    SPX = [[dataFrame['example1']['q1'][z], [dataFrame['example1']['q2'][z]], 1] for z in range(20)]
    X = [[dataFrame['example1']['q1'][z], [dataFrame['example1']['q2'][z]], 1] for z in range(20)]

    display(Sl(SPX), Pareto(PPX), X)


    APPX = [[dataFrame['example{}'.format(k)]['q1'][z], [dataFrame['example{}'.format(k)]['q2'][z]], 1] for k in range(1, 3) for z in range(20)]

    ASPX = [[dataFrame['example{}'.format(k)]['q1'][z], [dataFrame['example{}'.format(k)]['q2'][z]], 1] for k in range(1, 3) for z in range(20)]

    AX = [[dataFrame['example{}'.format(k)]['q1'][z], [dataFrame['example{}'.format(k)]['q2'][z]], 1] for k in range(1, 3) for z in range(20)]

    display(Sl(ASPX), Pareto(APPX), AX)