if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    sum3 = 0.0
    for i in range(n):
        sum3 = sum3 + a[i] * (i+1)*(n-i)
    print('%.2f' % sum3)
