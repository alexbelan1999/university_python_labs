import numpy as np


def change_array(arr, check):
    if check:
        max = 0
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if arr[i][j] > max:
                    max = arr[i][j]
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                arr[i][j] = max - arr[i][j]
        for i in arr:
            print(i)
    for i in range(0, len(arr)):
        min = np.inf
        for j in range(0, len(arr)):
            if arr[j][i] < min:
                min = arr[j][i]

        for k in range(0, len(arr)):
            arr[k][i] -= min
    for i in range(0, len(arr)):
        min = np.inf
        for j in range(0, len(arr)):
            if arr[i][j] < min:
                min = arr[i][j]

        for k in range(0, len(arr)):
            arr[i][k] -= min

    return arr


def array_for_algoritm(array):
    arr = []
    k = 0
    for i in range(2, len(array) + 2):
        arr.insert(k, [1, i, 1])
        k += 1

    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i][j] == 0:
                arr.insert(k, [i + 2, j + len(array) + 2, 1])
                k += 1

    for i in range(len(array) + 2, len(array) * 2 + 2):
        arr.insert(k, [i, 12, 1])
        k += 1

    return arr


def FordFalk(inputarr, checkarr, c):
    one = []
    for i in range(0, len(c)):
        one.insert(i, [])
        for j in range(0, len(c)):
            one[i].insert(j, 1)

    vertex = 12
    iteration = 0
    isBreak = False

    Y1 = None
    Y1_ = None

    while True:
        Y1 = []
        Y1_ = []
        iteration += 1
        markedEdge = [1]
        viewedEdge = [1]
        marks = [0] * (vertex + 1)
        marks[1] = [1, 0, np.inf]
        print(iteration, " итерация")
        while (vertex not in markedEdge):
            edge_ = markedEdge[0]
            if (edge_ < 7):
                print("Просмотр S", edge_ - 1, " вершины")
            else:
                print("   Просмотр t", edge_ - len(c) - 1, " вершины")

            newEdges = []
            for i in range(0, len(checkarr)):
                if ((edge_ == checkarr[i][0]) and (checkarr[i][1] not in viewedEdge) and (checkarr[i][2] > 0) and
                        marks[edge_][2] != 0):
                    markedEdge.append(checkarr[i][1])
                    viewedEdge.append(checkarr[i][1])
                    marks[checkarr[i][1]] = [checkarr[i][1], edge_, min(marks[edge_][2], checkarr[i][2])]
                    newEdges.append(checkarr[i][1])

                elif ((edge_ == checkarr[i][1]) and (checkarr[i][0] not in viewedEdge) and (
                        checkarr[i][2] < inputarr[i][2])):
                    markedEdge.append(checkarr[i][0])
                    viewedEdge.append(checkarr[i][0])
                    marks[checkarr[i][0]] = [checkarr[i][0], edge_,
                                             min(marks[edge_][2], inputarr[i][2] - checkarr[i][2])]
                    newEdges.append(checkarr[i][0])
            for i in range(0, len(newEdges)):
                if (newEdges[i] < 7):
                    print("Добавили вершину S", newEdges[i] - 1, ": [", marks[newEdges[i]][1], ", ",
                          marks[newEdges[i]][2], "]")
                else:
                    print("Добавили вершину t", newEdges[i] - len(c) - 1, ": [", marks[newEdges[i]][1], ", ",
                          marks[newEdges[i]][2], "]")

            Y1.append(edge_)
            if (edge_ < 7):
                print("Вершина S", edge_ - 1, " просмотрена")
            else:
                print("Вершина t", edge_ - len(c) - 1, " просмотрена")
            markedEdge.pop(0)

            if (len(markedEdge) == 0) and (vertex not in viewedEdge):
                isBreak = True
                break

        if isBreak:
            break

        print(" ")
        print("----------Шаг 2----------")

        arr_route = []
        arr_route.append("t")
        route = vertex
        flow = marks[route][2]

        while (route != 1):
            for i in range(0, len(checkarr)):
                if (checkarr[i][0] == marks[route][1] and checkarr[i][1] == route):
                    checkarr[i][2] -= flow
                    route = checkarr[i][0]
                    if (route < 7):
                        snumber = "S" + str(route - 1)
                        arr_route.append(snumber)
                    else:
                        snumber = "t" + str(route - len(c) - 1)
                        arr_route.append(snumber)

                    if (route < len(c) + 2) and (route > 1):
                        w = checkarr[i][0] - 2
                        ws = checkarr[i][1] - len(c) - 2
                        one[w][ws] = 0
                    break

                elif (checkarr[i][1] == abs(marks[route][1]) and checkarr[i][0] == route):
                    checkarr[i][2] += flow
                    route = checkarr[i][1]

                    if (route < 7):
                        snumber = "S" + str(route - 1)
                        arr_route.append(snumber)
                    else:
                        snumber = "t" + str(route - len(c) - 1)
                        arr_route.append(snumber)

                    if (route < len(c) * 2 + 2) and (route > len(c) + 1):
                        w = checkarr[i][0] - 2
                        ws = checkarr[i][1] - len(c) - 2
                        one[w][ws] = 1

                    break

        arr_route.reverse()
        str_route = (" ---> ").join(str(x) for x in arr_route)
        print(str_route)
        print("Увеличиваем поток на ", flow)
        print(" ")
    print(" ")
    for i in range(1, vertex + 1):
        if (i not in Y1):
            Y1_.append(i)

    fluxCheck = 0
    weight = 0

    for i in range(0, len(checkarr)):
        if (checkarr[i][0] in Y1) and (checkarr[i][1] in Y1_) and (checkarr[i][2] == 0):
            fluxCheck += inputarr[i][2]
            weight += inputarr[i][2]

    print("d = ", weight)
    answer = []
    answer.append(len(c) - weight)
    answer.append(Y1)
    answer.append(Y1_)
    answer.append(one)
    return answer


def some(c, c1, task_var):
    task1 = change_array(c, task_var)
    print("C2")
    for i in task1:
        print(i)
    nu = 100
    while (nu > 0):
        inputarr = array_for_algoritm(task1)
        checkarr = array_for_algoritm(task1)
        answer = FordFalk(inputarr, checkarr, c)
        Y1 = answer[1]
        Y1_ = answer[2]
        nu = answer[0]

        work = []
        workers = []

        if (nu == 0):
            checkarr = answer[3]
            for i in range(0, len(c)):
                for j in range(0, len(c)):
                    if (checkarr[i][j] == 0) and (j not in workers):
                        workers.append(j)
                        # mass =[]
                        mass = [i, j, c1[i][j]]
                        # print(work[i][2])
                        # mass.append(mass)
                        work.append(mass)
            end_answer = 0
            for i in range(0, len(c)):
                print(work[i][2])
                end_answer += work[i][2]
                print('Работа ', work[i][0] + 1, ' -> исполнитель ', work[i][1] + 1)

            print(end_answer)
            exit(0)
        min = np.inf
        for i in range(0, len(c)):
            for j in range(0, len(c)):
                if ((i + 2) in Y1) and ((j + len(c) + 2) in Y1_) and (task1[i][j] < min):
                    min = task1[i][j]

        for i in range(0, len(c)):
            for j in range(0, len(c)):
                if ((i + 2) in Y1):
                    task1[i][j] -= min

                if ((j + len(c) + 2) in Y1):
                    task1[i][j] += min

        print('C2~~')
        for i in task1:
            print(i)
    pass


def FordFalk_task3(inputarr, checkarr, c, c1):
    weight = 0
    s = []
    for i in range(0, len(c1)):
        s.insert(i, i + 1)

    t = [0] * 5

    vertex = 12
    iteration = 0
    isBreak = False

    while True:
        iteration += 1
        markedEdge = [1]
        viewedEdge = [1]
        marks = [0] * (vertex + 1)
        marks[1] = [1, 0, np.inf]
        print(iteration, " итерация")
        while (vertex not in markedEdge):
            edge_ = markedEdge[0]
            if (edge_ < 7):
                print("Просмотр S", edge_ - 1, " вершины")
            else:
                print("   Просмотр t", edge_ - len(c) - 1, " вершины")

            newEdges = []
            for i in range(0, len(checkarr)):
                if ((edge_ == checkarr[i][0]) and (checkarr[i][1] not in viewedEdge) and (checkarr[i][2] > 0) and
                        marks[edge_][2] != 0):
                    markedEdge.append(checkarr[i][1])
                    viewedEdge.append(checkarr[i][1])
                    marks[checkarr[i][1]] = [checkarr[i][1], edge_, min(marks[edge_][2], checkarr[i][2])]
                    newEdges.append(checkarr[i][1])

                elif ((edge_ == checkarr[i][1]) and (checkarr[i][0] not in viewedEdge) and (
                        checkarr[i][2] < inputarr[i][2])):
                    markedEdge.append(checkarr[i][0])
                    viewedEdge.append(checkarr[i][0])
                    marks[checkarr[i][0]] = [checkarr[i][0], edge_,
                                             min(marks[edge_][2], inputarr[i][2] - checkarr[i][2])]
                    newEdges.append(checkarr[i][0])
            for i in range(0, len(newEdges)):
                if (newEdges[i] < 7):
                    print("Добавили вершину S", newEdges[i] - 1, ": [", marks[newEdges[i]][1], ", ",
                          marks[newEdges[i]][2], "]")
                else:
                    print("Добавили вершину t", newEdges[i] - len(c) - 1, ": [", marks[newEdges[i]][1], ", ",
                          marks[newEdges[i]][2], "]")

            if (edge_ < 7):
                print("Вершина S", edge_ - 1, " просмотрена")
            else:
                print("Вершина t", edge_ - len(c) - 1, " просмотрена")
            markedEdge.pop(0)

            if (len(markedEdge) == 0) and (vertex not in viewedEdge):
                isBreak = True
                break

        if isBreak:
            break

        print(" ")
        print("----------Шаг 2----------")

        arr_route = []
        arr_route.append("t")
        route = vertex
        flow = marks[route][2]

        while (route != 1):
            for i in range(0, len(checkarr)):
                if (checkarr[i][0] == marks[route][1] and checkarr[i][1] == route):
                    r = route
                    checkarr[i][2] -= flow
                    route = checkarr[i][0]
                    numb = route - 2
                    if (route < 7):
                        snumber = "S" + str(route - 1)
                        arr_route.append(snumber)
                    else:
                        snumber = "t" + str(route - len(c) - 1)
                        arr_route.append(snumber)

                    if (route <= len(c1) + 1) and (route > 1):
                        t[numb] = r - len(c1) - 1
                    break

                elif (checkarr[i][1] == abs(marks[route][1])) and (checkarr[i][0] == route):
                    checkarr[i][2] += flow
                    numb = route - 2
                    route = checkarr[i][1]

                    if (route < 7):
                        snumber = "S" + str(route - 1)
                        arr_route.append(snumber)
                    else:
                        snumber = "t" + str(route - len(c) - 1)
                        arr_route.append(snumber)
                    break

        arr_route.reverse()
        weight += flow
        str_route = (" ---> ").join(str(x) for x in arr_route)
        print(str_route)
        print("Увеличиваем поток на ", flow)
        print(" ")
    print(" ")

    answer = []
    answer.append(len(c) - weight)
    answer.append(s)
    answer.append(t)
    return answer


def some_3(P0, c, c1):
    nu = 0
    while (nu < 1):
        FP0_arr = []
        for i in range(0, len(c1)):
            FP0_arr.insert(i, c1[P0[0][i] - 1][P0[1][i] - 1])

        FP0 = np.inf
        for i in range(0, len(FP0_arr)):
            if (FP0_arr[i] < FP0):
                FP0 = FP0_arr[i]
        print()
        print("Новое назначение")
        for i in P0:
            print(i)
        c3 = []

        for i in range(0, len(c1)):
            c3.insert(i, [])
            for j in range(0, len(c1)):
                if c1[i][j] <= FP0:
                    c3[i].insert(j, '*')
                else:
                    c3[i].insert(j, 0)
        print()
        print("C0")
        for i in c3:
            print(i)

        c3_3 = array_for_algoritm(c3)
        c3_3_clone = array_for_algoritm(c3)
        answer = FordFalk_task3(c3_3, c3_3_clone, c, c1)
        nu = answer[0]
        s = answer[1]
        t = answer[2]

        print("Результат для назначения")
        for i in P0:
            print(i)
        for i in range(0, len(c1)):
            if t[i]:
                P0[0][i] = s[i]
                P0[1][i] = t[i]

    pass
