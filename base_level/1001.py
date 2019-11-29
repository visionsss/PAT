def fun(n, count):
    if n == 1:
        return count
    if n % 2 == 0:
        return fun(n//2, count+1)
    else:
        return fun((3*n+1)//2, count+1)


if __name__ == '__main__':
    x = int(input())
    r = fun(x, 0)
    print(r)