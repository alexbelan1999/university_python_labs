import numpy as np

import func

matrix1 = [[1, 1.2, 2, 0.5],
           [1.2, 1, 0.5, 1],
           [2, 0.5, 2, 1.5],
           [0.5, 1, 1.5, 0.5]]

matrix2 = [[1, 1.2, 2, 0.5],
           [1.2, 1, 0.5, 1],
           [2, 0.5, 2, 1.5],
           [0.5, 1, 1.5, 0.5]]

matrix3 = [[-21.1, -35.8, -53.8, -39.2],
           [-7.88, 2.437, 31.5, 10.06],
           [17.13, 17.56, 6.25, 10.44],
           [7.375, 9.063, 8.0, 11.44]]

# matrix1 = [[2.2, 1, 0.5, 2],
#            [1, 1.3, 2, 1],
#            [0.5, 2, 0.5, 1.6],
#            [2, 1, 1.6, 2]]
#
# matrix2 = [[2.2, 1, 0.5, 2],
#            [1, 1.3, 2, 1],
#            [0.5, 2, 0.5, 1.6],
#            [2, 1, 1.6, 2]]
# matrix3 = [[2, 1, 1],
#            [1, 2.5, 1],
#            [1, 1, 3]]

var = int(input("Введите номер задания: "))

if var == 1:
    s = []
    for i in matrix1:
        print(i)
    number1 = len(matrix1)
    s = func.danilamethod(matrix1, number1, s)
    lmd = []
    E = 0.001

    a = -2
    b = -1
    lmd.append(func.dix(a, b, E))

    a = 0
    b = 0.5
    lmd.append(func.dix(a, b, E))

    a = 0.5
    b = 1
    lmd.append(func.dix(a, b, E))

    a = 4
    b = 5
    lmd.append(func.dix(a, b, E))

    # a = -2
    # b = 0
    # lmd.append(func.dix(a, b, E))
    #
    # a = 0
    # b = 1
    # lmd.append(func.dix(a, b, E))
    #
    # a = 1
    # b = 2
    # lmd.append(func.dix(a, b, E))
    #
    # a = 5
    # b = 6
    # lmd.append(func.dix(a, b, E))

    print("Собственные значения: ")
    for i in lmd:
        print(i)

    Y = []

    for i in range(0, len(lmd)):
        deg = number1 - 1
        Y.append(func.vectors(lmd, deg, i, number1))

        print('Вектор фробениуса ', i + 1)
        for j in Y[i]:
            print(j)

        F = []
        for j in range(0, number1):
            F.insert(j, [])

        for l in range(0, number1):
            F[l].insert(0, Y[i][l])

        X = np.dot(s, F)

        print('X = S * Y вектор: ', i + 1)
        for j in X:
            print(j)

        print('A * X: ')
        AX = np.dot(matrix2, X)
        for j in AX:
            print(j)

        print('Умножение lmbda[', (i + 1), '] * X')
        LX = np.dot(lmd[i], X)
        for j in LX:
            print(j)
elif var == 2:
    for i in matrix3:
        print(i)
    number2 = len(matrix3)
    E = float(input("Введите погрешность: "))
    func.step(matrix3, number2, E)

else:
    print("Ошибка выбора варинта!")
