if __name__ == '__main__':
    n, *a = list(map(int, input().split()))
    temp = 0
    for i, value in enumerate(a):
        if value-temp >= 0:
            a[i] = (value - temp)*6+5
        else:
            a[i] = (temp-value)*4+5
        temp = value
    print(sum(a))
