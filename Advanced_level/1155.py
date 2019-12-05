

"""
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<stack>
using namespace std;
int n;
vector<int> v;
stack<int> s;
vector<int> vvv;
int left(int i){return 2*i;}
int right(int i){return 2*i+1;}
bool judge_min(){
	for(int i=1;i<=v.size();i++){
		int l=left(i), r=right(i);
		if(l<=n){
			if(v[i]>v[l]) return false;
		}
		if(r<=n){
			if(v[i]>v[r]) return false;
		}
	}
	return true;
}
bool judge_max(){
	for(int i=1;i<=v.size();i++){
		int l=left(i), r=right(i);
		if(l<=n){
			if(v[i]<v[l]) return false;
		}
		if(r<=n){
			if(v[i]<v[r]) return false;
		}
	}
	return true;
}
void print(int i){
	vvv.push_back(v[i]);
	int l =left(i),r=right(i);
	if(r<=n){
		print(r);
	}
	else if(l>n){
		for(int j=0;j<vvv.size();j++){
			if(j==vvv.size()-1)
				printf("%d",vvv[j]);
			else
				printf("%d ",vvv[j]);
		}
		printf("\n");
		vvv.pop_back();
		return ;
	}
	if(l<=n){
		print(l);
	}
	else{
		for(int j=0;j<vvv.size();j++){
			if(j==vvv.size()-1)
				printf("%d",vvv[j]);
			else
				printf("%d ",vvv[j]);
		}
		printf("\n");
		vvv.pop_back();
		return ;
	}
	vvv.pop_back();
}
int main(){
	scanf("%d",&n);
	v.push_back(0);
	for(int i=1;i<=n;i++){
		int vv;
		scanf("%d",&vv);
		v.push_back(vv);
	}
	print(1);
	if(judge_max()){
		printf("Max Heap");
	}
	else if(judge_min()){
		printf("Min Heap");
	}
	else
		printf("Not Heap");
	return 0;
}
"""