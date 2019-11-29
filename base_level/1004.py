class student:
    def __init__(self, name, number, score):
        self.name = name
        self.number = number
        self.score = int(score)

    def __str__(self):
        return self.name + ' ' + self.number

    def __lt__(self, other):
        return self.score < other.score


if __name__ == '__main__':
    n = int(input())
    student_list = []
    for i in range(n):
        name, number, score = input().split(' ')
        student_list.append(student(name, number, score))
    student_list.sort()
    print(student_list[-1])     # 最高分
    print(student_list[0])  # 最低分
