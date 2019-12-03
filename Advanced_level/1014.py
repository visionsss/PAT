"""
只过了1个测试点，别抄
"""
class customer:
    def __init__(self, id, time):
        self.id = id
        self.time = time
        self.answer = 0

    def __lt__(self, other):
        return self.time < other.time

    def __str__(self):
        return self.id


if __name__ == '__main__':
    n, m, k, q = map(int, input().split())
    consume_time = list(map(int, input().split()))
    query_list = list(map(int, input().split()))
    customer_list = []
    for i, time in enumerate(consume_time):
        customer_list.append(customer(i+1, time))
    # 先填满人排队
    wait_list = [[] for i in range(m)]
    kk = k
    for i in range(m):
        for j in range(n):
            if i*n+j < kk:
                wait_list[i].append(customer_list.pop(0))
                k = k - 1

    # 等时间走人
    answer_list = []
    t = 0
    while k != 0 or t > 540:
        k = k - 1
        min1 = min(wait_list[0])
        t = t + min1.time
        index = wait_list[0].index(min1)
        wait_list[0][index].answer = t
        answer_list.append(wait_list[0][index])
        tt1 = min1.time
        for i in range(n):
            wait_list[0][i].time = wait_list[0][i].time - tt1
        for i in range(1, m):
            wait_list[i-1][index] = wait_list[i][index]
        wait_list[-1][index] = customer_list.pop(0)

    for i in range(n):
        t1 = 0
        for j in range(m):
            try:
                t1 = t1 + wait_list[j][i].time
                # print(t, t1)
                wait_list[j][i].answer = t + t1
                answer_list.append(wait_list[j][i])
            except:
                pass
                print('error')
    answer_list = sorted(answer_list, key=lambda x: int(x.id))
    # for i in answer_list:
    #     print(i.id, i.answer)
    for i in query_list:
        times = answer_list[i-1].answer
        if times > 540:
            print('Sorry')
        else:
            hour = str((times // 60) + 8)
            min_s = str(times % 60)
            if len(hour) < 2:
                hour = '0' + hour
            if len(min_s) < 2:
                min_s = '0' + min_s
            # print(answer_list[i-1].id)
            print(f'{hour}:{min_s}')

