if __name__ == '__main__':
    answer = []
    n = int(input())
    for i in range(1, n+1):
        x, y, z = map(int, input().split(' '))
        if x + y > z:
            answer.append(f'Case #{i}: true')
        else:
            answer.append(f'Case #{i}: false')

    for j in answer:
        print(j)
