def fun(s, num):
    r = 0
    for i, value in enumerate(s[::-1]):
        if '0' <= value <= '9':
            r += int(value) * (int(num)**i)
        else:
            r += (ord(value)-ord('a')+10) * (int(num) ** i)
    return r
if __name__ == '__main__':
    n1, n2, tag, radix = input().split()
    if tag == '1':
        number = fun(n1, int(radix))
        other_number = n2
    else:
        number = fun(n2, int(radix))
        other_number = n1
    flag = 0
    i_max = 999999999   # 数太小有个测试点过不去
    i_min = 2
    xx = 2
    for i in other_number:
        xx = max(ord(i), xx)
    if chr(xx).isalpha():
        i_min = max(i_min, 1+int(xx-ord('a'))+10)
    else:
        i_min = max(i_min, int(chr(xx))+1)
    # print(i_min)
    while i_min < i_max:
        i_mid = ((i_max-i_min) // 2) + i_min

        x = fun(other_number, i_mid)
        # print(i_min, i_mid, i_max)
        # print(other_number, x)
        if len(other_number) == 1:
            print(i_min)
            flag = 1
            break
        if x == number:
            flag = 1
            print(i_mid)
            break
        elif x > number:
            i_max = i_mid
        else:
            i_min = i_mid + 1
    if not flag:
        print('Impossible')
