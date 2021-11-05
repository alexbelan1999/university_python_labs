import numpy as np

V = [[0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1],
     [0, 1, 0, 1, 0],
     [1, 1, 1, 1, 1]]
print(V)
V1 = [0, 0, 0, 0, 0]
flag = False
for i in range(0, 4):
    for j in range(i + 1, 4):
        print("(", i + 1, ",", j + 1, ")")
        for k in range(0, 5):
            V1[k] = V[i][k] ^ V[j][k]

        print(V1)
        for l in range(0, 4):
            flag = False
            if V[l] == V1:
                print(True)
                flag = True
                break
if flag == True:
    print("Код соответствует подгруппе")
else:
    exit(-1)
