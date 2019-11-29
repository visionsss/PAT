import copy


def get_number_list(nu):
    ret = []
    while nu != 1:
        if nu % 2 == 0:
            nu = nu // 2
        else:
            nu = (3 * nu + 1) // 2
        ret.append(nu)
    ret = set(ret)
    return ret


if __name__ == '__main__':
    n = int(input())
    num_list = input().split(' ')
    num_list = set(map(int, num_list))
    num_list_copy = copy.deepcopy(num_list)
    for num in num_list_copy:
        r = get_number_list(num)
        k = r & num_list
        # print(num_list, r, k)
        for kk in k:
            num_list.remove(kk)

    num_list = list(num_list)
    num_list.sort(reverse=True)
    num_list = str(num_list)
    print(num_list[1: -1].replace(',', ''))

