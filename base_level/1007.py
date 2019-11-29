def judge(k):
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            return False
    return True


def count_p(k):
    up = 2
    count = 0
    num = 3
    while k >= num:
        if judge(num):
            if num - up == 2:
                count += 1
            up = num
            num += 2    # +1的话会超时，呵呵，所以+2，因为偶数（除2外）肯定不是素数
        else:
            num += 2
    return count


if __name__ == '__main__':
    n = int(input())
    print(count_p(n))
