import math
import numpy

str = input("Введите строку для шифрования: ")
str1 = str.replace(" ", "")
print("Введенная строка: ", str1)
lenstr = len(str1)
print("Длина строки: ", lenstr)

if (lenstr % 2 != 0):
    lenstr = lenstr + 1
    str1 = str1 + " "

print("Выбираем  размер таблицы.")
n = 3.0
m = 0
while (n < lenstr):
    if (lenstr % n == 0):
        print(n)

        break
    n = n + 1
m = lenstr / n
print(n, " ", m)
testarr = [['-'] * int(m) for i in range(int(n))]
# testarr = numpy.empty((int(n),int(m)))
i = 0
k = 0
while (i < n):

    if ((i + 1) % 2 == 0):
        j = int(m - 1)
        while (j >= 0):
            testarr[i][j] = str1[k]
            k = k + 1
            j = j - 1
    else:
        j = 0
        while (j < m):
            testarr[i][j] = str1[k]
            k = k + 1
            j = j + 1
    i = i + 1
print(testarr[0])
print(testarr[1])
print(testarr[2])
