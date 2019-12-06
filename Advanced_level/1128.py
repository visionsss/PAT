# 最后一个测试点超时，不代表我的代码错哈，用C就不回超时
if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        flag = 0
        n, *q_list = map(int, input().split())
        for i, value in enumerate(q_list):
            for j in range(0, i):
                if value == q_list[j] or abs(i-j) == abs(q_list[i]-q_list[j]):
                    flag = 1
                    break
            if flag:
                break
        if flag:
            print('NO')
        else:
            print("YES")
"""
用C写AC
#include<iostream>
#include<math.h>
#include<vector>
using namespace std;
int main(){
	int n,k;
	cin>>k;
	for(int i=0;i<k;i++){
		scanf("%d",&n);
		int flag = 0;
		vector<int> in(n+2);
		for(int j=0;j<n;j++){
			scanf("%d", &in[j]);
			for(int jj=0;jj<j;jj++){
				if(in[j]==in[jj] || abs(j-jj)==abs(in[j]-in[jj])){
					flag = 1;
					break;
				}
			}
		}
		if(flag==1) printf("NO\n");
		else  printf("YES\n");
	}
	return 0; 
}
python第一版超时
def judge(r, c):
    for ii in range(n):
        if array[r][ii] == 1 and ii != c:
            return False
    for ii in range(n):
        if array[ii][c] == 1 and ii != r:
            return False
    x = max(r, c, n-r, n-c)
    for ii in range(-x, x):
        rr1 = r + ii
        rr2 = r - ii
        cc1 = c + ii
        cc2 = c - ii
        if 0 <= rr1 < n and 0 <= cc1 < n:
            if rr1 != r and cc1 != c:
                if array[rr1][cc1] == 1:
                    return False
        if 0 <= rr2 < n and 0 <= cc2 < n:
            if rr2 != r and cc2 != c:
                if array[rr2][cc2] == 1:
                    return False
    return True


def check():
    for ii in range(n):
        for jj in range(n):
            if array[ii][jj] == 1:
                if not judge(ii, jj):
                    return False
    return True


if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        n, *q_list = map(int, input().split())
        array = [[0 for ii in range(n)] for iii in range(n)]
        for col, row in enumerate(q_list):
            array[-row][col] = 1
        if check():
            print('YES')
        else:
            print('NO')
"""