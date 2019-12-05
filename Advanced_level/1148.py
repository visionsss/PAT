if __name__ == '__main__':
    n = int(input())
    v = [0]     # 说的话
    for i in range(n):
        v.append(int(input()))
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            a = [1 for k in range(n+1)] # 实际情况1为好人，-1为狼人
            lie = []    # 撒谎的人
            a[i] = a[j] = -1    #   这两个为狼人
            for k in range(1, n+1):
                if v[k]*a[abs(v[k])] < 0:
                    lie.append(k)
            if len(lie) == 2 and a[lie[0]] + a[lie[1]] == 0:    # 撒谎的是一个好人一个狼人with 2 werewolves among them, at least one but not all the werewolves were lying, and there were exactly 2 liars
                print(f'{i} {j}')
                exit(0)
    print('No Solution')