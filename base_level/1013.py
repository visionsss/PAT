def judge(k):
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            return False
    return True


def get_prime_list(k):
    count = 1
    prime_list = [2]
    num = 3
    while count < k:
        if judge(num):
            prime_list.append(num)
            count += 1
            num += 2    # +1的话会超时，呵呵，所以+2，因为偶数（除2外）肯定不是素数
        else:
            num += 2
    return prime_list


if __name__ == '__main__':
    m, n = map(int, input().split(' '))
    answer_list = get_prime_list(n)[m-1:]
    for i, num in enumerate(answer_list):
        if i+1 == len(answer_list):
            print(num, end='')
        elif (i+1) % 10 == 0:
            print(num)
        else:
            print(num, end=' ')


