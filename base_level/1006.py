if __name__ == '__main__':
    n = int(input())
    a = n // 100     # 百位
    b = (n % 100) // 10     # 十位
    c = n % 10  # 个位
    for i in range(a):
        print('B', end='')
    for i in range(b):
        print('S', end='')
    for i in range(1, c+1):
        print(i, end='')
