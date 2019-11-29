class student:
    l = 0
    h = 0

    def div_class(self):
        if self.score1 >= student.h and self.score2 >= student.h:
            return 4
        elif self.score1 >= student.h > self.score2:
            return 3
        elif self.score1 < student.h and self.score2 < student.h:
            if self.score1 > self.score2:
                return 2
            else:
                return 1
        else:
            return 1

    def __init__(self, num, score1, score2):
        self.num = num
        self.score1 = score1    # 德分
        self.score2 = score2    # 才分

    def __lt__(self, other):
        if self.div_class() < other.div_class():
            return True
        elif self.div_class() > other.div_class():
            return False
        else:
            if self.score1+self.score2 < other.score1+other.score2:
                return True
            elif self.score1+self.score2 > other.score1+other.score2:
                return False
            else:
                if self.score1 == other.score1:
                    if self.score2 == other.score2:
                        return self.num > other.num
                    else:
                        return self.score2 < other.score2
                else:
                    return self.score1 < other.score1


if __name__ == '__main__':
    n, student.l, student.h = map(int, input().split())
    student_list = []
    for i in range(n):
        num, score1, score2 = map(int, input().split())
        if score1 >= student.l and score2 >= student.l:
            student_list.append(student(num, score1, score2))
    print(len(student_list))
    student_list.sort(reverse=True)
    for i in student_list:
        print(f'{i.num} {i.score1} {i.score2}')
"""
python 三个测试超时
附上c的ac的代码
#include<stdio.h>
#include<algorithm> 

using namespace std;
struct student{
	int num;
	int score1; // 德分
	int score2; //才分
	int all; //总分 
}s[100010];
bool cmp(student a, student b){
	if(a.all!=b.all){
		return a.all>b.all;
	}
	else if(a.score1!=b.score1){
		return a.score1>b.score1;
	}
	else{
		return a.num < b.num;
	}
}
int main(){
	int n,l,h;
	scanf("%d%d%d",&n,&l,&h);
	for(int i=0;i<n;i++){
		scanf("%d%d%d",&s[i].num,&s[i].score1,&s[i].score2);
		s[i].all = s[i].score1 + s[i].score2;
	}
	sort(s, s+n, cmp);
	
	// 计算个数
	int count = 0;
	for(int i=0;i<=n;i++){
		if(s[i].score1>=l && s[i].score2>=l)
			count++;
	} 
	printf("%d\n",count);
	// 打印第一种人 德分和才分均不低于此线的被定义为“才德全尽”
	for(int i=0;i<n;i++){
		if(s[i].score1>=h && s[i].score2>=h){
			printf("%d %d %d\n",s[i].num, s[i].score1, s[i].score2);
		}
	} 
	// 打印第二种人 才分不到但德分到线的一类考生属于“德胜才”
	for(int i=0;i<n;i++){
		if(s[i].score1>=h && s[i].score2<h && s[i].score1>=l && s[i].score2>=l){
			printf("%d %d %d\n",s[i].num, s[i].score1, s[i].score2);
		}
	} 
	// 打印第三种人 德才分均低于 H 德分不低于才分
	for(int i=0;i<n;i++){
		if(s[i].score1<h && s[i].score2<h&&s[i].score1>=s[i].score2 && s[i].score1>=l && s[i].score2>=l){
			printf("%d %d %d\n",s[i].num, s[i].score1, s[i].score2);
		}
	} 
	// 打印第四种人
	for(int i=0;i<n;i++){
		if(s[i].score1<h && s[i].score1<s[i].score2 && s[i].score1>=l && s[i].score2>=l){
			printf("%d %d %d\n",s[i].num, s[i].score1, s[i].score2);
		}
	} 
	
	return 0;
} 
"""



