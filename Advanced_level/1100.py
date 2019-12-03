def earth2mars(n):
    n = int(n)
    if n <= 12:
        return li[n]
    else:
        a = n // 13
        b = n % 13
        if b == 0:
            return ol[a]
        else:
            return ol[a] + ' ' + li[b]


def mars2earth(s):
    if len(s.split()) == 1:
        try:
            return li.index(s)
        except:
            return ol.index(s)*13
    else:
        a, b = s.split()
        return ol.index(a)*13 + li.index(b)


if __name__ == '__main__':
    li = ['tret', 'jan', 'feb', 'mar', 'apr', 'may',
          'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
    ol = ['', 'tam', 'hel', 'maa', 'huh', 'tou', 'kes',
          'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
    # 测试所有结果是否正确
    # for i in range(169):
    #     print(i, earth2mars(f'{i}'), mars2earth(earth2mars(f'{i}')))
    n = int(input())
    for i in range(n):
        inp = input()
        if inp[0].isdigit():
            print(earth2mars(inp))
        else:
            print(mars2earth(inp))