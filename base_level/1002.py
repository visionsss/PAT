def add(n):
    re = 0
    for i in n:
        re = re + int(i)
    return re


def print_y(n, count):
    if count == len(y)-1:
        print(num_list[int(n)], end='')
    else:
        print(num_list[int(n)], end=' ')


if __name__ == '__main__':
    # 注意 999999999991 = 100输出yi ling ling
    # x = '1234567890987654321123456789'
    x = input()
    num_list = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
    y = str(add(x))
    for count, i in enumerate(y):
        print_y(i, count)
