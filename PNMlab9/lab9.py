import math
import numpy as np

testarr = np.array([[0.21, -0.18, 0.75, 2.1], [0.13, 0.75, -0.11, 1.3], [3.01, -0.33, 0.11, 2.68]])
print(testarr)


def calcGauss(arr, k):
    n = len(arr)
    if n == k:
        return arr

    k1 = 0
    maxelement = -1
    i = k
    while (i < n):
        if (abs(arr[i][k]) > maxelement):
            maxelement = abs(arr[i][k])
            k1 = i
        i = i + 1

    print("max: ", maxelement)
    buff = np.copy(arr[k1])

    arr[k1] = np.copy(arr[k])
    arr[k] = np.copy(buff)
    print(arr)

    det1 = arr[k][k]
    j = k
    while (j < n + 1):
        arr[k][j] = arr[k][j] / det1
        j = j + 1

    i = k + 1
    while (i < n):
        det2 = arr[i][k]
        j = k
        while (j < n + 1):
            arr[i][j] = -1 * arr[k][j] * det2 + arr[i][j]
            j = j + 1
        i = i + 1
    print(arr)
    arr = calcGauss(arr, k + 1)
    return arr


def mainelementGauss():
    n = len(testarr)
    k = 0
    arr = np.zeros((n, n + 1))
    arrX = np.zeros(n)
    i = 0
    while (i < n):
        j = 0
        while (j < n + 1):
            arr[i][j] = testarr[i][j]
            j = j + 1
        i = i + 1
    print(arr)
    n = len(arr)
    arr = calcGauss(arr, 0)
    i = n - 1
    while (i >= 0):
        arrX[i] = arr[i][n]
        j = i + 1
        while (j < n):
            arrX[i] -= arr[i][j] * arrX[j]
            j = j + 1
        i = i - 1
    print("Вектор X: ")
    t = 0
    while (t < len(arrX)):
        print(arrX[t])
        t = t + 1
    pass


def DjardanoGauss():
    n = len(testarr)
    k = 0
    arr = np.zeros((n, n + 1))
    arrX = np.zeros(n)
    i = 0
    while (i < n):
        j = 0
        while (j < n + 1):
            arr[i][j] = testarr[i][j]
            j = j + 1
        i = i + 1
    print(arr)
    k = 0
    while (k < n):
        det1 = arr[k][k]
        arrprev = np.copy(arr)
        i = 0
        while (i < n):
            det2 = arr[i][k]
            j = 0
            while (j < n + 1):
                if ((i != k) & (j != k)):
                    arr[i][j] = arr[i][j] - arrprev[k][j] / det1 * det2
                else:
                    if ((i == k) & (j != k)):
                        arr[i][j] = arrprev[k][j] / det1
                    else:
                        if ((i != k) & (j == k)):
                            arr[i][j] = 0
                        else:
                            arr[i][j] = 1
                j = j + 1
            i = i + 1
            print(arr)
        k = k + 1
    i = 0
    while (i < n):
        arrX[i] = arr[i][n]
        i = i + 1
    print("Вектор X: ")
    t = 0
    while (t < len(arrX)):
        print(arrX[t])
        t = t + 1
    pass


print("Метод Гаусса с выбором главного элемента")
mainelementGauss()
print("Метод Жордана-Гаусса")
DjardanoGauss()
