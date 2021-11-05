import numpy as np


def func(x):
    # return x * x * x * x - 6 * x * x * x - 0.2 * x * x + 12.735 * x - 2.7616
    return pow(x, 4) - 4.5 * pow(x, 3) - 2.190000000000005 * x * x + 5.624999999999997 * x - 1.0124999999999993


def startm(number):
    c = []
    for i in range(0, number):
        c.insert(i, [])
        for j in range(0, number):
            if i != j:
                c[i].insert(j, 0)
            else:
                c[i].insert(j, 1)
    return c


def danilamethod(matrix, number, s):
    print('Метод Данилевского')
    count = number - 2
    res = []
    matrixarraym = []

    while count >= 0:
        mright = startm(number)
        mleft = startm(number)
        for i in range(0, len(matrix)):
            if i == count:
                mright[count][i] = 1 / matrix[count + 1][count]
            else:
                mright[count][i] = (-1) * (matrix[count + 1][i] / matrix[count + 1][count])

        for i in range(0, len(matrix)):
            mleft[count][i] = matrix[count + 1][i]

        multiply = np.dot(mleft, matrix)
        res = np.dot(multiply, mright)
        matrixarraym.append(mright)

        print('mright')
        for i in mright:
            print(i)

        print('mleft')
        for i in mleft:
            print(i)

        print('res')
        for i in res:
            print(i)

        for i in range(0, number):
            for j in range(0, number):
                matrix[i][j] = res[i][j]

        count -= 1

    cof = []
    s = matrixarraym[0]

    for i in range(0, number):
        cof.insert(i, res[0][i])

    for j in range(1, number - 1):
        print()
        for k in matrixarraym[j]:
            print(k)
        s = np.dot(s, matrixarraym[j])

    print('cof: ', cof)
    print('S:')
    for i in s:
        print(i)
    strfunc = 'x^'
    strfunc += str(number)
    c = number - 1

    for i in range(0, number):
        if cof[i] > 0:
            strfunc += '-' + str(cof[i]) + 'x^' + str(c)

        else:
            strfunc += '+' + str((-1) * cof[i]) + 'x^' + str(c)
        c -= 1

    print('func: ', ''.join(strfunc))
    return s


def dix(a, b, E):
    iter = 0
    print("Метод дихотамии")

    while ((b - a) / 2 >= E):
        c = (a + b) / 2
        fa = func(a)
        fc = func(c)

        print(a, "  ", b, "  ", c, "  ", fc)
        if (fc < 0 and fa < 0) or (fc > 0 and fa > 0):
            a = c
        else:
            b = c
        iter += 1

    print("Корень = ", c, " с точностью ", E, " количество итераций ", iter)
    return c


def vectors(lmd, deg, j, number):
    vec = []
    for i in range(0, number):
        vec.insert(i, pow(lmd[j], deg))
        deg -= 1

    return vec


def step(matrix, number, E):
    print("Степенной метод: ")
    # Y0 = [[1], [1], [1]]
    Y0 = [[1], [1], [1], [1]]
    print("Y0:")
    for i in Y0:
        print(i)
    Y1, Y2 = [], []
    l1, l2, newl = 0, 0, 0
    res = []
    count = 1
    Y1 = np.dot(matrix, Y0)
    l1 = Y1[0][0] / Y0[0][0]
    l2 = l1
    while abs(l2 - newl) > E:
        newl = l1
        Y2 = np.dot(matrix, Y1)
        print("Y:")
        for i in Y2:
            print(i)
        l2 = Y2[0][0] / Y1[0][0]
        Y1 = Y2[0:len(Y2)]
        l1 = l2
        count += 1

    print("Количество итераций равно ", count)
    print("Наибольшее собственное значение = ", l2)
    print("Собственный вектор: ")
    for i in Y2:
        print(i)
    pass
