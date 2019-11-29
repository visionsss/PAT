if __name__ == '__main__':
    a = list(map(float, input().split()[1:]))
    b = list(map(float, input().split()[1:]))
    dict_a = dict()
    for i in range(0, len(a), 2):
        if str(int(a[i])) in dict_a:  # 存在就+
            dict_a[str(int(a[i]))] += a[i+1]
        else:
            dict_a[str(int(a[i]))] = a[i + 1]

    for i in range(0, len(b), 2):
        if str(int(b[i])) in dict_a:  # 存在就+
            dict_a[str(int(b[i]))] += b[i + 1]
        else:
            dict_a[str(int(b[i]))] = b[i + 1]

    answer_list = []
    num = len(dict_a)
    for item in sorted(map(int, dict_a.keys()), reverse=True):
        if dict_a[str(item)] == 0:
            num -= 1
        else:
            answer_list.append(item)
            answer_list.append(dict_a[str(item)])
    if num == 0:
        print('0')
    else:
        print(num, end=' ')
        for i in range(len(answer_list)):
            if i == len(answer_list) - 1:
                print('%.1f'%answer_list[i], end='')
            elif i % 2 == 0:
                print(answer_list[i], end=' ')
            else:
                print('%.1f' % answer_list[i], end=' ')
"""
用字典，存在的就系数相加，不存在的就直接加上去
注意：
输出一定要标准化 会存在0.1+0.1=0.20000001的情况
keys排序输出
0的时候输出0
注意负数
测试用例：
4 7 516.6 6 969.5 5 289.5 2 894.3
8 10 409.7 7 374.8 6 132.1 5 405.7 4 804.9 3 678.7 2 191.2 0 11.6
8 10 409.7 7 891.4 6 1101.6 5 695.2 4 804.9 3 678.7 2 1085.5 0 11.6
"""

