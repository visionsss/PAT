def judge1(s):
    for ii in s:
        if ii != 'P' and ii != 'A' and ii != 'T':
            return False
    if 'P' in s and 'A' in s and 'T' in s:
        if s.count('P') == 1 and s.count('T') == 1:
            if s.index('T') > s.index('P')+1:
                return True
            else:
                return False
        return False
    else:
        return False


def change(s):
    p_index = 0
    t_index = 0
    for i, chr in enumerate(s):
        if chr == 'P':
            p_index = i
        elif chr == 'T':
            t_index = i
    while True:
        a = s[:p_index]
        b = s[p_index+1: t_index]
        c = s[t_index+1:]
        if len(b) > 1 and len(c) >= len(a):
            s = a + 'P' + b[:-1] + 'T' + c[:len(c)-len(a)]
            t_index = t_index - 1
        else:
            break
    if len(a) == len(c):
        return True
    else:
        return False


def judge(s):
    if judge1(s):
        if change(s):
            return True
    return False


if __name__ == '__main__':
    answer = []
    n = int(input())
    for i in range(n):
        string = input()
        if judge(string):
            answer.append('YES')
        else:
            answer.append('NO')
    for i in answer:
        print(i)
    # s = 'AAPAATAAAA'
    # print(change(s))