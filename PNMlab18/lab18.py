import func
import numpy as np

matrix = [[9, 11, 6],
          [-10, -14, -8],
          [3, 5.5, 3]]
# matrix = [[-16, -100, -190],
#           [96, 380, 704],
#           [-48, -182, -336]]
number = len(matrix)

QQQ = []
E = 0.01
cont = 0
print('--- ИТЕРАЦИЯ № 1 ---')
A = func.QRMethod(matrix, number, QQQ)
while func.sumsquarediag(A) > E:
    cont += 1
    print('--- ИТЕРАЦИЯ № ', (cont + 1), ' ---')
    A = func.QRMethod(A, number, QQQ)
lmd = []
print('Собственные значения')

for i in range(0, number):
    print('lambda', (i + 1), ': ', A[i][i])
    lmd.append(A[i][i])
for i in range(0, number):
    A[i][i] = A[i][i] - lmd[i]
print("A - lamda*E: ")
for i in A:
    print(i)
print("Определитель:", np.linalg.det(A))
