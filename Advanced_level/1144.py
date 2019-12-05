if __name__ == '__main__':
    n = input()
    num_list = list(map(int, input().split()))
    d = {}
    for i in num_list:
        d[i] = 1
    for i in range(1, 99999999999):
        if d.get(i) is None:
            print(i)
            break

