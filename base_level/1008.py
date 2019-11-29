if __name__ == '__main__':
    # n, m = map(int, input().split(' ')) # 慎用map方法，pat会出现非零返回，就是程序报错
    s = input().split(' ')
    n = int(s[0])
    m = int(s[1])
    input_list = input().split(' ')

    m = m % n
    left = input_list[n-m:]
    right = input_list[:n-m]
    answer_list = ' '.join(left+right)
    print(answer_list)

