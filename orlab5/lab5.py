import func

plan = [[0, 1, 12], [0, 2, 9], [0, 6, 12],
        [1, 3, 10], [2, 4, 4], [3, 4, 0],
        [3, 7, 8], [4, 5, 9], [5, 6, 8],
        [5, 7, 5], [6, 7, 3]]

vertex = 8
T0 = func.getT0(plan, vertex)
print('T0: ', T0)

S = func.getS(T0, plan)
print('S: ', S)

T1 = func.getT1(plan, vertex, T0)
print('T1: ', T1)

P = func.getP(T1, plan, T0)
print('P: ', P)
