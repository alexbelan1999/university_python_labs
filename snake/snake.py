import math
import numpy

str = input("Введите строку для шифрования: ")
str1 = str.replace(" ", "")
print("Введенная строка: ", str1)
lenstr = len(str1)
print("Длина строки: ", lenstr)

if (lenstr % 2 != 0):
    lenstr = lenstr + 1

print("Выбираем  размер таблицы.")
n = 2.0
m = 0
while (n < lenstr):
    if (lenstr % n == 0):
        m = lenstr / n
        break
    n = n + 1
print(n, " ", m)
