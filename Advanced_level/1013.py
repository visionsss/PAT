def dfs(now):
    visited[now] = 1
    for ii in G[now]:
        if (not visited[ii]) and lost != ii:
            dfs(ii)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    G = []
    for i in range(n+1):
        G.append([])
    for i in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    lost_list = list(map(int, input().split()))
    for i in range(k):
        lost = lost_list[i]
        visited = [0 for ii in range(n+1)]
        count = -1
        for j in range(1, n+1):
            if lost == j:
                continue
            if not visited[j]:
                dfs(j)
                count += 1
        print(count)
"""
python 最后1个测试点超时
被迫用C重新写
#include<iostream>
#include<vector>
#include<memory.h>
using namespace std;
int n,m,k, lost;
vector<int> G[1005];
bool visited[1005];
void dfs(int now){
	visited[now]=true;
	for(int ii=0;ii<G[now].size();ii++){
		int v = G[now][ii];
		if(!visited[v] && v!=lost){
			dfs(v);
		}
	}
}
int main(){
	scanf("%d%d%d",&n,&m,&k);
	for(int i=0;i<m;i++){
		int a,b;
		scanf("%d%d",&a,&b);
		G[a].push_back(b);
		G[b].push_back(a);
	}
	for(int i=0;i<k;i++){
		memset(visited,false,sizeof(visited));
		int count = -1;
		scanf("%d",&lost);
		for(int j=1;j<=n;j++){
			if(j==lost)
				continue;
			if(!visited[j]){
				dfs(j);
				count++;
			}
		}
		printf("%d\n",count);
	}
	
	return 0; 
} 
"""