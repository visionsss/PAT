import copy


def judge(k):
    try:
        kk = float(k)
        if not -1000 <= kk <= 1000:
            return False
        if len(k.split('.')) == 2:
            if len(k.split('.')[-1]) > 2:
                return False
        return True
    except:
        return False


if __name__ == '__main__':
    n = int(input())
    inp = list(input().split(' '))
    inp_copy = copy.deepcopy(inp)
    for i in inp_copy:
        if not judge(i):
            inp.remove(i)
            print(f'ERROR: {i} is not a legal number')
    num = len(inp)
    if num == 0:
        print('The average of 0 numbers is Undefined')
    elif num == 1:
        inp = map(float, inp)
        sum1 = sum(inp)
        avg = sum1 / num
        print(f'The average of 1 number is %.2f' % avg)
    else:
        inp = map(float, inp)
        sum1 = sum(inp)
        avg = sum1 / num
        print(f'The average of {num} numbers is %.2f' % avg)
"""
有毒！！！！！
1的时候number没有s
有毒！！！！！
"""