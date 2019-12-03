def judge(n):
    # 判断n是不是素数
    i = 2
    if n == 1 or n == 0:
        return False
    while i*i < n+1:
        if n % i == 0:
            return False
        i += 1
    return True


def change(n, d):
    s = ''
    while n:
        s = s + str(n % d)
        n = n // d
    r = 0
    s = s[::-1]
    for i, value in enumerate(s):
        r = r + int(value) * d ** i
    return r


if __name__ == '__main__':
    while 1:
        k = input().split()
        if len(k) == 1:
            break
        a, b = map(int, k)
        c = change(a, b)    # 变
        # print(a, c)
        if judge(a) and judge(c):
            print('Yes')
        else:
            print('No')
