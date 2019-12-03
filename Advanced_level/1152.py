def judge(x):
    x = int(x)
    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True
    i = 2
    while i*i < x+1:
        if x % i == 0:
            return False
        i = i + 1
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    s = input()
    flag = 0
    for i in range(0, n-m+1):
        if judge(s[i: i+m]):
            flag = 1
            print(s[i: i+m])
            break
    if not flag:
        print('404')