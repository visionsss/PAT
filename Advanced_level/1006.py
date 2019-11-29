import datetime


class p1:
    def __init__(self, a, t1, t2):
        self.a = a
        self.t1 = t1
        self.t2 = t2

    def __lt__(self, other):
        return self.t1 < other.t1

    def __str__(self):
        return self.a


class p2:
    def __init__(self, a, t1, t2):
        self.a = a
        self.t1 = t1
        self.t2 = t2

    def __lt__(self, other):
        return self.t2 < other.t2

    def __str__(self):
        return self.a


if __name__ == '__main__':
    n = int(input())
    student1 = []
    student2 = []
    for i in range(n):
        a1, a2, a3 = input().split()
        b1, b2, b3 = map(int, a2.split(":"))
        c1, c2, c3 = map(int, a3.split(":"))
        a2 = datetime.time(b1, b2, b3)
        a32 = datetime.time(c1, c2, c3)
        student1.append(p1(a1, a2, a3))
        student2.append(p2(a1, a2, a3))
    student1.sort()
    student2.sort()
    print(student1[0], student2[-1])
