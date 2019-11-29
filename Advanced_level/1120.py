def fun(n):
    sum = 0
    str_n = str(n)
    for s in str_n:
        sum = sum+int(s)
    return sum


if __name__ == '__main__':
    n = input()
    in_list = list(map(int, input().split()))
    answer = set(list(map(fun, in_list)))
    answer = list(map(str, sorted(answer)))
    print(len(answer))
    print(' '.join(answer))
