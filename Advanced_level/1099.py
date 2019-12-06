class node:
    def __init__(self):
        self.key = -1
        self.right = -1
        self.left = -1


def in_order(root):
    if root == -1:
        return
    in_order(a[root].left)
    in_list.append(root)
    in_order(a[root].right)


def bfs(root):
    num = 0
    queue = [root]
    while len(queue) != 0:
        print(a[queue[0]].key, end='')
        num += 1
        if num != n:
            print(end=' ')
        root = queue[0]
        queue.pop(0)
        if a[root].left != -1:
            queue.append(a[root].left)
        if a[root].right != -1:
            queue.append(a[root].right)


a = [node() for i in range(100)]
n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    a[i].left = l
    a[i].right = r
data = list(map(int, input().split()))
data.sort()
in_list = []
in_order(0)
for i in range(n):
    a[in_list[i]].key = data[i]
bfs(0)
"""
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<stack>
#include <map>
#include<queue>
using namespace std;
struct{
	int key;
	int left;
	int right;
}a[105];
int n;
vector<int> data, in;
void inorder(int root){
	if(root==-1) return ;
	inorder(a[root].left);
	in.push_back(root);
	inorder(a[root].right);
}
void bfs(int root){
	int num=0;
	queue<int> q;
	q.push(root);
	while (!q.empty()){
		root = q.front();
		printf("%d",a[root].key);
		num++;
		if(num!=n) printf(" ");
		q.pop();
		if(a[root].left!=-1) q.push(a[root].left);
		if(a[root].right!=-1) q.push(a[root].right);
	}
}
int main(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i].left>>a[i].right;
	}
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		data.push_back(x);
	}
	sort(data.begin(),data.end());
	inorder(0);
	for(int i=0;i<n;i++) a[in[i]].key = data[i];
	bfs(0);
	return 0;
}
"""