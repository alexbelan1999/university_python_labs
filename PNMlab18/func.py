import numpy as np
import math


def sumsquarediag(matrix):
    sumnum = 0
    for i in range(1, len(matrix)):
        for j in range(0, i):
            sumnum += matrix[i][j] * matrix[i][j]

    res = np.sqrt(sumnum)
    print('sqrt(sum) = ', res)
    return res


def newmatrix(matrix, i):
    for j in range(i + 1, len(matrix)):
        matrix[j][i] = 0

    return matrix


def QRMethod(matrix, number, QQQ):
    B = matrix
    resmultmatrix = np.dot(1, matrix)
    kol = 0
    iteration = number - 1
    f = 0
    HHH = []
    AAA = []
    while (iteration > 0):
        print('------------ ШАГ ', (f + 1), '------------')
        F = []
        print('A', f)
        for i in resmultmatrix:
            print(i)

        for j in range(0, number):
            F.insert(j, [])
        for l in range(0, number):
            F[l].insert(0, resmultmatrix[l][f])

        if f > 0:
            for s in range(0, f):
                F[s][0] = 0

        sumf = 0
        for t in range(0, number):
            sumf = sumf + F[t][0] * F[t][0]

        S1 = np.sqrt(sumf)
        print('S1', S1)
        mu = math.pow(2 * S1 * (S1 - resmultmatrix[f][f]), (-1 / 2))
        print('mu', mu)

        F[f][0] = resmultmatrix[f][f] - S1
        print('Столбец')
        for i in F:
            print(i)
        W = np.dot(mu, F)
        print('W')
        for i in W:
            print(i)
        WT = []
        for i in range(0, number):
            WT.insert(i, W[i][0])
        WT = [WT]
        print('WT')
        print(WT)
        var = np.dot(W, WT)
        WWTx2 = np.dot(2, var)
        print('WWT')
        for i in WWTx2:
            print(i)

        E = []
        for j in range(0, number):
            E.insert(j, [])
        for l in range(0, number):
            for k in range(0, number):
                if (l == k):
                    E[l].insert(k, 1)
                else:
                    E[l].insert(k, 0)

        H = np.subtract(E, WWTx2)
        HHH.append(H)
        print('H')
        for i in H:
            print(i)
        resmultmatrix = np.dot(H, resmultmatrix)

        resmultmatrix = newmatrix(resmultmatrix, f)
        print('A-№', f + 1)
        for i in resmultmatrix:
            print(i)
        AAA.append(resmultmatrix)
        kol += 1
        iteration -= 1
        f += 1

    Q = HHH[0]
    R = AAA.pop()
    for i in range(1, len(HHH)):
        Q = np.dot(Q, HHH[i])

    print('Q')
    for i in Q:
        print(i)

    QQQ.append(Q)

    print('R')
    for i in R:
        print(i)

    print('QR-ПРОВЕРКА')
    for i in np.dot(Q, R):
        print(i)

    ares = np.dot(R, Q)

    print('ИТОГОВАЯ МАТРИЦА')
    for i in ares:
        print(i)
    return ares
