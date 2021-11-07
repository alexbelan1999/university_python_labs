import numpy as np


def maxdiag(matrix):
    maxnum = -np.inf
    I = 0
    K = 0

    for i in range(0, len(matrix)):
        for j in range(i + 1, len(matrix)):
            if abs(matrix[i][j]) > maxnum:
                I = i
                K = j
                maxnum = abs(matrix[i][j])

    res = []
    res.append(matrix[I][K])
    res.append(I)
    res.append(K)
    return res


def sumsquarediag(matrix):
    sumnum = 0
    for i in range(1, len(matrix)):
        for j in range(0, i):
            sumnum += matrix[i][j] * matrix[i][j]

    res = np.sqrt(sumnum)
    print('sqrt(sum) = ', res)
    return res


def matrixT1(number, SIN, COS, I, K):
    C = []
    for i in range(0, number):
        C.insert(i, [])
        for j in range(0, number):
            if i == j:
                C[i].insert(j, 1)
            else:
                C[i].insert(j, 0)

    C[I][K] = -SIN
    C[K][I] = SIN
    C[I][I] = COS
    C[K][K] = COS

    return C


def vectors(matrix, number, j):
    vec = []

    for i in range(0, number):
        vec.append(matrix[i][j])

    return vec


def rotation(matrix, matrix1, number, eps):
    B = matrix
    iteration = 0
    T0 = []
    AIK = 0
    while sumsquarediag(B) > eps:
        A = maxdiag(B)
        print("Максимальный по модулю над диагональный элемент: ", A)

        AIK = A[0]
        I = A[1]
        K = A[2]

        Z = np.sqrt(1 - (4 * AIK * AIK) / ((B[I][I] - B[K][K]) * (B[I][I] - B[K][K]) + 4 * AIK * AIK))
        print("Z: ", Z)

        C = np.sqrt((1 + Z) / 2)
        print("C: ", C)

        E = 1
        if B[I][I] == B[K][K]:
            E = np.sign(AIK)

        if B[I][I] != B[K][K]:
            E = np.sign((B[I][I] - B[K][K]) / AIK)

        print("E: ", E)

        S = np.sqrt((1 - Z) / 2) * E
        print("S:", S)

        T1 = matrixT1(number, S, C, I, K)

        T0.append(T1)
        TT = [[0] * number for i in range(number)]
        for i in range(0, number):
            for j in range(0, number):
                TT[j][i] = T1[i][j]

        mult = np.dot(TT, B)
        B = np.dot(mult, T1)
        B[K][I] = 0
        B[I][K] = 0
        print("T1: ")
        for i in T1:
            print(i)

        print("TT: ")
        for i in TT:
            print(i)

        print("B: ")
        for i in B:
            print(i)

        iteration += 1

    print('Количество итераций: ', iteration)

    for i in range(0, len(B)):
        print('lamda ', i + 1, '= ', B[i][i])

    XT = T0[0]
    for i in range(1, iteration):
        XT = np.dot(XT, T0[i])

    print('Таблица векторов')
    for i in XT:
        print(i)

    for i in range(0, number):
        vec = vectors(XT, number, i)
        print("Вектор X", i + 1, " (", vec, ")")

        F = []
        for j in range(0, number):
            F.insert(j, [])

        for l in range(0, number):
            F[l].insert(0, vec[l])

        print('A * X: ')
        AX = np.dot(matrix1, F)
        for j in AX:
            print(j)

        print('Умножение lmbda[', (i + 1), '] * X')
        LX = np.dot(B[i][i], F)
        for j in LX:
            print(j)
