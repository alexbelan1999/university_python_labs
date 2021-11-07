def getT0(plan, vertex):
    T0 = []
    T0.append(0)

    event = 1
    E = []

    while len(T0) != vertex:
        for i in range(0, len(plan)):
            if plan[i][1] == event:
                E.append(T0[plan[i][0]] + plan[i][2])

        maxnum = 0
        for i in range(0, len(E)):
            if maxnum < E[i]:
                maxnum = E[i]

        T0.append(maxnum)
        event += 1
        E.clear()

    return T0


def getS(T0, plan):
    S = []
    for i in range(0, len(plan)):
        S.append(T0[plan[i][1]] - T0[plan[i][0]] - plan[i][2])

    return S


def getT1(plan, vertex, T0):
    T1 = [0] * vertex
    T1[vertex - 1] = T0[vertex - 1]
    event = vertex - 2
    E = []
    E1 = [0] * vertex
    E1[vertex - 1] = 0
    while event:
        for i in range(0, len(plan)):
            if plan[i][0] == event:
                E.append(E1[plan[i][1]] + plan[i][2])

        maxnum = 0
        for i in range(0, len(E)):
            if maxnum < E[i]:
                maxnum = E[i]

        E1[event] = maxnum
        T1[event] = T0[vertex - 1] - maxnum
        event -= 1
        E.clear()

    T1[event] = 0
    return T1


def getP(T1, plan, T0):
    P = []
    for i in range(len(plan)):
        P.append(T1[plan[i][1]] - T0[plan[i][0]] - plan[i][2])
    return P
