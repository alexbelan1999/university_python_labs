import numpy as np

testarr = np.array([[1, 2, 3, -2], [2, -1, -2, -3], [3, 2, -1, 2], [2, -3, 2, 1]])
# testarr  = np.array([[1,0,1],[0,1,1],[1,1,0]])
print(testarr)
n = len(testarr)
arrE = np.eye(n)
testarr1 = np.zeros((n, n))
print(arrE)


def LU():
    n = len(testarr)

    arr = np.zeros((n, n))
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    i = 0
    while (i < n):
        j = 0
        while (j < n):
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
    detA = 1
    i = 0
    while (i < n):
        detA *= L[i][i]
        i = i + 1
    print("detA = ", round(detA))
    arrY = np.zeros((n, n))
    k = 0
    while (k < n):
        i = 0
        while (i < n):
            arrY[k][i] = arrE[i][k]
            j = 0
            while (j < i):
                arrY[k][i] -= L[i][j] * arrY[k][j]
                j = j + 1
            arrY[k][i] = arrY[k][i] / L[i][i]
            i = i + 1
        k = k + 1

    print("Y:")
    print(arrY.T)
    arrX = np.zeros((n, n))
    k = 0
    while (k < n):
        i = n - 1
        while (i >= 0):
            arrX[k][i] = arrY[k][i]
            j = i + 1
            while (j < n):
                arrX[k][i] -= U[i][j] * arrX[k][j]
                j = j + 1
            arrX[k][i] = arrX[k][i] / U[i][i]
            i = i - 1
        k = k + 1

    print("X: ")
    t = 0
    print(arrX.T)
    pass


def DjardanoGauss():
    n = len(testarr)
    k = 0
    arr = np.zeros((n, 2 * n))
    arrX = np.zeros((n, n))
    i = 0
    while (i < n):
        j = 0
        while (j < n):
            arr[i][j] = testarr[i][j]
            j = j + 1
        j = n
        while (j < 2 * n):
            arr[i][j] = arrE[i - n][j - n]
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
            while (j < 2 * n):
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
        j = n
        while (j < 2 * n):
            arrX[i - n][j - n] = arr[i][j]
            j = j + 1

        i = i + 1
    print("X: ")
    print(arrX)
    print("A * A^(-1)")
    print(np.matmul(testarr, arrX))
    pass


print("LU-разложение")
LU()
print("Метод Жордана-Гаусса")
DjardanoGauss()
