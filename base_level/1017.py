if __name__ == '__main__':
    a, b = map(int, input().split())
    q = a//b
    r = a%b
    print(f'{q} {r}')