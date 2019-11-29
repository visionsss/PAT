def fun1():
    sum1 = 0
    flag = 0
    for i in x:
        if int(i) % 10 == 0:
            flag = 1
            sum1 = sum1 + int(i)
    if flag:
        return sum1
    else:
        return 'N'


def fun2():
    sum2 = 0
    k = 1
    flag = 0
    for i in x:
        if i % 5 == 1:
            flag = 1
            sum2 = sum2 + k * i
            k = -1*k
    if flag:
        return sum2
    else:
        return 'N'


def fun3():
    sum3 = 0
    flag = 0
    for i in x:
        if i % 5 == 2:
            sum3 += 1
            flag = 1
    if flag:
        return sum3
    else:
        return 'N'


def fun4():
    sum4 = []
    flag = 0
    for i in x:
        if i % 5 == 3:
            sum4.append(i)
            flag = 1
    if flag:
        return round(sum(sum4)/len(sum4), 1)
    else:
        return 'N'


def fun5():
    max5 = -1
    for i in x:
        if i % 5 == 4:
            max5 = max(i, max5)
    if max5 == -1:
        return 'N'
    else:
        return max5


if __name__ == '__main__':
    x = input().split()[1:]
    x = list(map(int, x))
    a1 = fun1()
    a2 = fun2()
    a3 = fun3()
    a4 = fun4()
    a5 = fun5()
    print(a1, a2, a3, a4, a5)
