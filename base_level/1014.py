a1 = input()
a2 = input()
b1 = input()
b2 = input()
result = []
sum = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for i in range(min(len(a1), len(a2))):
    if (a1[i] == a2[i]) and ('A' <= a1[i] <= 'G'):
        result.append(ord(a1[i])-ord('A'))
        break
for j in range(i+1, (min(len(a1), len(a2)))):
    if (a1[j] == a2[j]) and ('A' <= a1[j] <= 'N'):
        result.append(str(ord(a1[j])-ord('A')+10))
        break
    elif (a1[j] == a2[j]) and ('0' <= a1[j] <= '9'):
        result.append('0'+a1[j])
        break
for i in range(min(len(b1), len(b2))):
    if b1[i].isalpha() and (b1[i] == b2[i]):
        if i < 10:
            result.append('0'+str(i))
        else:
            result.append(str(i))
        break
print(f"{sum[result[0]]} {result[1]}:{result[2]}")
