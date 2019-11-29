
if __name__ == '__main__':
    a, b = map(int, input().split())
    if a + b < 0:
        print('-', end='')
    c = str(abs(a + b))[::-1]
    re = []
    for i in range(len(c)):
        if i % 3 == 2 and i != len(c)-1:
            re.insert(0, c[i])
            re.insert(0, ',')
        else:
            re.insert(0, c[i])
    print(''.join(re))
