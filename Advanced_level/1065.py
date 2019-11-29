if __name__ == '__main__':
    n = int(input())
    answer_list = []
    for i in range(n):
        a, b, c = map(int, input().split())
        if a + b > c:
            answer_list.append(f'Case #{i+1}: true')
        else:
            answer_list.append(f'Case #{i+1}: false')
    for i in range(n):
        print(answer_list[i])