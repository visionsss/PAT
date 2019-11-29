def fun(p_order, i_order, depth):
    """
    后序遍历 左右中
    中序遍历 左中右
    :param p_order: 后续遍历序列
    :param i_order: 中续遍历序列
    :param depth: 深度
    :return:
    """
    if len(p_order) == 0:
        return
    num = p_order[-1]
    # insert answer
    for i in range(30):
        if answer[depth][i] == 0:
            answer[depth][i] = num
            break
    index = i_order.index(num)
    i_order1 = i_order[:index]
    i_order2 = i_order[index+1:]
    p_order1 = p_order[:len(i_order1)]
    p_order2 = p_order[len(i_order1):-1]
    fun(p_order1, i_order1, depth+1)
    fun(p_order2, i_order2, depth + 1)


if __name__ == '__main__':
    n = int(input())
    post_order = input().split()
    in_order = input().split()
    answer = [[0 for i in range(30)] for j in range(30)]
    fun(post_order, in_order, 0)
    r = []
    for i in answer:
        for j in i:
            if j != 0:
                r.append(str(int(j)))
    print(' '.join(r))

