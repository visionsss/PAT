if __name__ == '__main__':
    a, b, c, d = input().split()
    x1 = a.count(b)
    x2 = c.count(d)
    try:
        b = int(b*x1)
    except:
        b = 0
    try:
        d = int(d * x2)
    except:
        d = 0
    print(b+d)

