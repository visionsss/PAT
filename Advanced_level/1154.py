def judge(c_list):
    for i, color in enumerate(c_list):
        for j in vector[i]:
            if color == c_list[j]:  # 连接的地图颜色相同，则返回False
                return False
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    vector = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        vector[a].append(b)
        vector[b].append(a)
    k = int(input())
    for i in range(k):
        color_list = list(map(int, input().split()))
        if judge(color_list):
            print(f'{len(set(color_list))}-coloring')
        else:
            print('No')
"""
C语言代码
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
int n,m,k;
vector<int> a[10005];
vector<int> color_list;
bool judge(){
	for(int i=0;i<color_list.size();i++){
		int value1 = color_list[i];
		for(int j=0;j<a[i].size();j++){
			int value2 = color_list[a[i][j]];
			if(value1 == value2)
				return false;
		}
	}
	return true;
}
int main(){
	cin>>n>>m;
	for(int i=0;i<m;i++){
		int x1,x2;
		scanf("%d %d",&x1,&x2);
		a[x1].push_back(x2);
		a[x2].push_back(x1);
	}
	cin>>k;
	for(int i=0;i<k;i++){
		int color;
		set<int> s;
		for(int j=0;j<n;j++){
			scanf("%d",&color);
			color_list.push_back(color);
			s.insert(color);
		}
		if(judge()){
			printf("%d-coloring\n",s.size());
		}
		else
			printf("No\n");
		s.clear();
		color_list.clear(); 
	}
	return 0;
}
"""