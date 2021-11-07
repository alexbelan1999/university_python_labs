import math

import numpy as np

testarr = np.array([[1, 2, 3, 4, 1], [1, 2, 3, 4, 1], [4, 3, 2, 1, 3],[4, 3, 2, 1, 3]])
# testarr = np.array([[5.7, -7.8, -5.6, -8.3, 2.4], [6.6, 13.1, -6.3, 4.3, -5.5], [14.7, -2.8, 5.6, -12.1, 8.6],
#                     [18.5, 12.7, -23.7, 5.7, 14.7]])
# testarr = np.array([[5.7,-7.8,-5.6,-8.3,2.4],[14.7,-2.8,5.6,-12.1,8.6],[14.7,-2.8,5.6,-12.1,8.6],[14.7,-2.8,5.6,-12.1,8.6]])
# testarr = np.array([[1,0,0,0,1],[0,0,1,0,2],[1,0,0,0,1],[0,0,0,1,3]])
number = 0
print(testarr)
flag = False


def directGauss(flag, number):
    flag = False
    number = 0
    n = len(testarr)
    m = len(testarr[0])
    i = 0
    arr = np.zeros((n, m))
    while (i < n):
        j = 0
        while (j < m):
            arr[i][j] = testarr[i][j]
            j = j + 1
        i = i + 1
    k = 0
    while (k < n):

        det1 = arr[k][k]
        if (arr[k][k] == 0):
            number = k + 1
            arr1 = np.copy(arr)
            arr1[0] = arr[0]
            arr1[1] = arr[1]
            arr1[2] = arr[2]
            arr1[3] = np.zeros(5)
            flag = True
            print(arr1)
            return arr1, number, flag
        j = k
        while (j < m):
            arr[k][j] = arr[k][j] / det1
            j = j + 1
        i = k + 1
        while (i < n):
            det2 = arr[i][k]
            j = k
            while (j < m):
                arr[i][j] = round((-1 * arr[k][j] * det2 + arr[i][j]), 4)
                j = j + 1
            i = i + 1
        print(arr)
        i = 0
        while (i < n):
            zero = 0
            j = 0
            while (j < m):
                if (arr[i][j] == 0):
                    zero = zero + 1
                j = j + 1
            if (zero == m):
                l = i
                while (l < n - 1):
                    arr[l] = arr[l + 1]
                    l = l + 1
                n = n - 1
                i = i - 1
                k = k - 1

            i = i + 1

        k = k + 1
    print(arr)
    return arr, number, flag


def reverseGauss(arr, flag, number):
    zero = 0
    n = len(arr)
    m = len(arr[n - 1])
    arrX = np.empty(n)
    arrY = np.zeros((n, m))
    arrX1 = np.full(n, "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    i = 0
    while (i < n):
        zero = 0
        j = 0
        while (j < m):
            if (arr[i][j] == 0 or math.isnan(arr[i][j])):
                zero = zero + 1
            j = j + 1
        if ((zero == m - 1) & (arr[i][m - 1] != 0)):
            print("Нет решений!")
            exit(0)
        else:
            if (zero == m):
                k = i
                while (k < n - 1):
                    arr[k] = arr[k + 1]
                    k = k + 1
                n = n - 1
                i = i - 1

        i = i + 1
    if (n == m - 1):
        i = n - 1
        while (i >= 0):

            arrX[i] = arr[i][m - 1]
            j = i + 1
            while (j < m - 1):
                arrX[i] -= arr[i][j] * arrX[j]
                j = j + 1
            i = i - 1
    else:
        if (n < m - 1):
            print("Бесконечное множество решений!")
            if (flag == True):
                i = n - 1
                while (i >= 0):
                    l = -1
                    arrY[i][0] = arr[i][m - 1]

                    k = m - 2
                    while (k >= n):
                        l += 2
                        arrY[i][l] = -arr[i][k]
                        arrY[i][l + 1] = k + 1
                        k = k - 1
                    k = n - 1

                    i = i - 1

                i = 0
                while (i < n):
                    if (number - 1 == 0):
                        print("x[2] = ", arrY[i][0], " + x", number)
                        print("x[3] = ", arrY[i + 1][0], " + x", number)
                        print("x[4] = ", arrY[i + 2][0], " + x", number)
                        break
                    if (number - 1 == 1):
                        print("x[1] = ", arrY[i][0], " + x", number)
                        print("x[3] = ", arrY[i + 1][0], " + x", number)
                        print("x[4] = ", arrY[i + 2][0], " + x", number)
                        break
                    if (number - 1 == 2):
                        print("x[1] = ", arrY[i][0], " + x", number)
                        print("x[2] = ", arrY[i + 1][0], " + x", number)
                        print("x[4] = ", arrY[i + 2][0], " + x", number)
                        break
                    if (number - 1 == 3):
                        print("x[1] = ", arrY[i][0], " + x", number)
                        print("x[2] = ", arrY[i + 1][0], " + x", number)
                        print("x[3] = ", arrY[i + 2][0], " + x", number)
                        break

                    i = i + 1
                exit(0)
            i = n - 1
            while (i >= 0):
                l = -1
                arrY[i][0] = arr[i][m - 1]

                k = m - 2
                while (k >= n):
                    l += 2
                    arrY[i][l] = -arr[i][k]
                    arrY[i][l + 1] = k + 1
                    k = k - 1
                k = n - 1

                while (k > i):
                    arrY[i][0] -= arr[i][k] * arrY[k][0]

                    j = 1
                    while (j <= l):
                        arrY[i][j] -= arr[i][k] * arrY[k][j]
                        j += 2
                    k = k - 1

                arrX1[i] = arrY[i][0]
                j = 1
                while (j <= l):
                    arrX1[i] += " + " + str(arrY[i][j]) + " x" + str(arrY[i][j + 1])
                    j += 2

                i = i - 1
            i = 0
            print("Столбец X: ")
            while (i < n):
                print("x[", i + 1, "] = ", arrX1[i])
                i = i + 1
            exit(0)
    print(arr)
    print("Столбец X: ")
    t = 0
    while (t < len(arrX)):
        print(arrX[t])
        t = t + 1
    pass


def LU():
    n = len(testarr)

    arr = np.zeros((n, n + 1))
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    i = 0
    while (i < n):
        j = 0
        while (j < n + 1):
            arr[i][j] = testarr[i][j]
            j = j + 1
        i = i + 1
    i = 0
    while (i < n):
        U[i][i] = 1
        i = i + 1
    k = 0
    while (k < n):
        i = 0
        while (i < n):
            if (k <= i):
                L[i][k] = arr[i][k]
                j = 0
                while (j < k):
                    L[i][k] -= L[i][j] * U[j][k]
                    j = j + 1
            else:
                U[i][k] = arr[i][k]
                j = 0
                while (j < i):
                    U[i][k] -= L[i][j] * U[j][k]
                    j = j + 1
                U[i][k] = U[i][k] / L[i][i]
            i = i + 1

        k = k + 1
    print("Матрица L")
    print(L)
    print("Матрица U")
    print(U)
    arrY = np.zeros((n, n))
    i = 0
    while (i < n):
        arrY[i] = arr[i][n]
        j = 0
        while (j < i):
            arrY[i] -= L[i][j] * arrY[j]
            j = j + 1
        arrY[i] = arrY[i] / L[i][i]
        i = i + 1
    print("Вектор Y:")
    print(arrY)
    arrX = np.zeros((n, n))
    i = n - 1
    while (i >= 0):
        arrX[i] = arrY[i]
        j = i + 1
        while (j < n):
            arrX[i] -= U[i][j] * arrX[j]
            j = j + 1
        arrX[i] = arrX[i] / U[i][i]
        i = i - 1
    print("Столбец X: ")
    t = 0
    while (t < len(arrX)):
        print(arrX[t][0])
        t = t + 1
    pass


print("Метод Гаусса")
myarr, number, flag = directGauss(flag, number)
print("reverse")
reverseGauss(myarr, flag, number)
print("LU-разложение")
LU()
