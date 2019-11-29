if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    r_sum = -1
    temp = 0
    temp_index = 0
    l = 0
    r = n-1
    for i, value in enumerate(a):
        temp = temp + value
        if temp < 0:
            temp = 0
            temp_index = i + 1
        elif r_sum < temp:
            r = i
            l = temp_index
            r_sum = temp
    if r_sum < 0:
        r_sum = 0

    print(r_sum, a[l], a[r])

