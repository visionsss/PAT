if __name__ == "__main__":
    line = input().split(" ")
    num = int(line[0])
    dic1 = {}
    for x in range(num):
        dic1[int(line[2 * x + 1])] = float(line[2 * x + 2])

    line = input().split(" ")
    num = int(line[0])
    dic2 = {}
    for x in range(num):
        dic2[int(line[2 * x + 1])] = float(line[2 * x + 2])
    dic1 = {key: value for key, value in dic1.items() if value != 0}
    dic2 = {key: value for key, value in dic2.items() if value != 0}

    result = [[x, 0] for x in range(2001)]
    for x in dic1:
        for i in dic2:
            result[x + i][1] += dic1[x] * dic2[i]
    output = str(len([x for x in result if x[1] != 0])) + " "

    for x in result[::-1]:
        if x[1] != 0:
            output = output + str(x[0]) + " " + "{:.1f}".format(x[1]) + " "
    print(output[:-1])
