import math


def rsa(n, e, w):
    print('n = ', n, 'e = ', e, 'w = ', w)
    p = 2
    q = 0
    while (p < n):
        if (n % p == 0):
            q = n / p
            break
        p = p + 1
    fi = (p - 1) * (q - 1)
    nod = fi + 1
    d = 0
    while (1 > 0):
        # print(nod)
        if (nod % e == 0):
            d = nod / e
            break
        else:
            nod += fi
    print("p = ", p, " q = ", q, " fi = ", fi, " d = ", d)
    d1 = d
    arrbin = []
    i = 0
    while (d1 != 0):
        arrbin.insert(i, d1 % 2)
        # print(arrbin[i])
        d1 = (d1 - arrbin[i]) / 2
        i = i + 1

    c = 1
    arrmod = []
    arrmod.insert(0, w % n)
    # print(arrmod[0])
    j = 1
    while (j < i):
        arrmod.insert(j, math.pow(arrmod[j - 1], 2) % n)
        # print(arrmod[j])
        j = j + 1
    j = 0
    while (j < len(arrbin)):
        if (arrbin[j] == 1):
            c *= arrmod[j]
        j = j + 1

    c = c % n
    print("c = ", c)
    print()
    pass


rsa(21, 7, 13)
rsa(589, 7, 109)
rsa(3338287, 19683, 2092819)
