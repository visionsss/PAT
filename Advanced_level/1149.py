if __name__ == '__main__':
    n, m = map(int, input().split())
    incompatible_dict = {}
    for i in range(n):
        key, value = input().split()
        if not incompatible_dict.get(key) is None:
            incompatible_dict[key].append(value)
        else:
            incompatible_dict[key] = [value]
        if not incompatible_dict.get(value) is None:
            incompatible_dict[value].append(key)
        else:
            incompatible_dict[value] = [key]

    for i in range(m):
        length, *goods_list = input().split()
        flag = 0
        for j in goods_list:
            if not incompatible_dict.get(j) is None:
                for k in goods_list:
                    if k == j:
                        continue
                    if k in incompatible_dict[j]:
                        print('No')
                        flag = 1
                        break
            if flag == 1:
                break
        if flag == 0:
            print('Yes')

