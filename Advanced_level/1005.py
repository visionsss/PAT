if __name__ == '__main__':
    x = input()
    count = 0
    for i in x:
        count += int(i)
    dig = ['zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']
    str_count = str(count)
    for i in range(len(str_count)):
        if i + 1 == len(str_count):
            print(dig[int(str_count[i])], end='')
        else:
            print(dig[int(str_count[i])], end=' ')