a = input().split()
x = []
i = 0
while i < len(a):
    m = int(a[i])*int(a[i+1])
    n = int(a[i+1]) - 1
    i += 2
    if n == -1:
        continue
    x.append(str(m))
    x.append(str(n))
if len(x) == 0:
    print('0 0')
else:
    print(' '.join(x).strip())

