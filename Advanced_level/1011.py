if __name__ == '__main__':
    a = list(map(float, input().split()))
    b = list(map(float, input().split()))
    c = list(map(float, input().split()))
    r_list = ['W', 'T', 'L']
    answer1 = []
    answer2 = []
    answer2.append(max(a))
    answer1.append(r_list[a.index(max(a))])
    answer2.append(max(b))
    answer1.append(r_list[b.index(max(b))])
    answer2.append(max(c))
    answer1.append(r_list[c.index(max(c))])

    for i in answer1:
        print(i, end=' ')
    sum1 = 1
    for i in answer2:
        sum1 = sum1 * i
    sum1 = (sum1*0.65-1) * 2
    print(round(sum1, 2), end='')