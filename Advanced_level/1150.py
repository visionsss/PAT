def check(c_list):
    sum_v = 0
    for i in range(len(c_list)-1):
        if G[city_list[i]][city_list[i+1]] == 0:
            return 0
        else:
            sum_v += G[city_list[i]][city_list[i+1]]
    return sum_v


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(m):
        c1, c2, dist = map(int, input().split())
        G[c1][c2] = G[c2][c1] = dist
    m = int(input())
    shortest = 99999999
    short_index = 0
    for i in range(m):
        k, *city_list = map(int, input().split())
        city_set = set(city_list)
        dis = check(city_list)
        if not dis: # 连续不通
            print(f'Path {i+1}: NA (Not a TS cycle)')
        elif city_list[0] == city_list[-1] and len(city_set) == n and k == n+1: # 刚刚好是一个环
            print(f'Path {i+1}: {dis} (TS simple cycle)')
            if dis and dis < shortest:
                short_index = i + 1
                shortest = dis
        elif city_list[0] == city_list[-1] and len(city_set) == n:  # 多几个环
            print(f'Path {i + 1}: {dis} (TS cycle)')
            if dis and dis < shortest:
                short_index = i + 1
                shortest = dis
        else:
            print(f'Path {i + 1}: {dis} (Not a TS cycle)')
    print(f'Shortest Dist({short_index}) = {shortest}')
