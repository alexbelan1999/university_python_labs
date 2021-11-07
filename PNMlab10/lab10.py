import math
import numpy as np

# testarr = np.array([[2.65, -1.27, 0.18, 2.25],[-1.27, 2.73, -0.46, 0.93],[0.18, -0.46, 2.16, 1.33]])
testarr = np.array([[4.31, 0.26, 0.61, 0.27, 1.02],
                    [0.26, 2.32, 0.18, 0.34, 1.0],
                    [0.61, 0.18, 3.2, 0.31, 1.34],
                    [0.27, 0.34, 0.31, 5.17, 1.27]])
print(testarr)


def squareMethod():
    n = len(testarr)
    arr = np.zeros((n, n + 1))
    arrS = np.zeros((n, n))
    i = 0
    while (i < n):
        j = 0
        while (j < n + 1):
            arr[i][j] = testarr[i][j]
            j = j + 1
        i = i + 1
    print("Матрица S")
    i = 0
    while (i < n):
        j = i
        while (j < n):
            if (i == j):
                arrS[i][i] = arr[i][i]
                k = 0
                while (k < i):
                    arrS[i][i] -= (arrS[k][i] ** 2)
                    k = k + 1
                # print(arrS[i][i])
                arrS[i][i] = arrS[i][i] ** 0.5

            else:
                arrS[i][j] = arr[i][j]
                det = 0
                k = 0
                while (k < i):
                    det += arrS[k][i] * arrS[k][j]
                    k = k + 1
                arrS[i][j] = (arrS[i][j] - det) / arrS[i][i]
            print(arrS)
            j = j + 1
        i = i + 1
    print("Матрица S")
    print(arrS)
    print("Матрица ST")
    print(arrS.T)
    print("ST * S")
    print(np.matmul(arrS.T, arrS))
    arrY = np.zeros(n)
    i = 0
    while (i < n):
        arrY[i] = arr[i][n]
        j = 0
        while (j < i):
            arrY[i] -= arrS[j][i] * arrY[j]
            j = j + 1
        arrY[i] = arrY[i] / arrS[i][i]
        i = i + 1
    print("Столбец Y")
    for t in arrY:
        print(t)
    arrX = np.zeros(n)
    i = n - 1
    while (i >= 0):
        arrX[i] = arrY[i]
        j = i + 1
        while (j < n):
            arrX[i] -= arrS[i][j] * arrX[j]
            j = j + 1
        arrX[i] = arrX[i] / arrS[i][i]
        i = i - 1
    print("Столбец X")
    for t in arrX:
        print(t)
    pass


squareMethod()
