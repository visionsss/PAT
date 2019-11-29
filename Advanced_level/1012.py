import copy
if __name__ == '__main__':
    n, m = map(int, input().split())
    id_list = []
    A_list = []
    C_list = []
    M_list = []
    E_list = []
    for i in range(n):
        ids, c, mm, e = input().split()
        id_list.append(ids)
        A_list.append(int(c)+int(mm)+int(e))
        C_list.append(int(c))
        M_list.append(int(mm))
        E_list.append(int(e))
    A_list_index = copy.deepcopy(A_list)
    C_list_index = copy.deepcopy(C_list)
    M_list_index = copy.deepcopy(M_list)
    E_list_index = copy.deepcopy(E_list)
    A_list.sort(reverse=True)
    C_list.sort(reverse=True)
    M_list.sort(reverse=True)
    E_list.sort(reverse=True)
    A_list_index = list(map(lambda x: A_list.index(x)+1, A_list_index))
    C_list_index = list(map(lambda x: C_list.index(x)+1, C_list_index))
    M_list_index = list(map(lambda x: M_list.index(x)+1, M_list_index))
    E_list_index = list(map(lambda x: E_list.index(x)+1, E_list_index))
    # 查找
    answer1 = []
    answer2 = []
    for i in range(m):
        ids = input()
        try:
            index = id_list.index(ids)
            A = A_list_index[index]
            C = C_list_index[index]
            M = M_list_index[index]
            E = E_list_index[index]
            l = min(A, C, M, E)
            if A == l:
                answer1.append(A)
                answer2.append('A')
            elif C == l:
                answer1.append(C)
                answer2.append('C')
            elif M == l:
                answer1.append(M)
                answer2.append('M')
            else:
                answer1.append(E)
                answer2.append('E')

        except:
            # 找不到该学生
            answer1.append('N/A')
            answer2.append('')

    for i in range(m):
        if answer1[i] == 'N/A':
            print(answer1[i])
        else:
            print(answer1[i], answer2[i])
"""
多提交几次就过了，时间刚刚好
"""