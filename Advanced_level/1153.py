class node:
    def __init__(self, string, score):
        self.string = string
        self.level = string[0]
        self.site = string[1:4]
        self.date = string[4:10]
        self.rank = string[10:]
        self.score = int(score)

    def __str__(self):
        return self.string + ' ' + str(self.score)

    def __lt__(self, other):
        if self.score == other.score:
            return self.string > other.string
        return self.score < other.score


class node2:
    def __init__(self, site, num):
        self.site = site
        self.num = num

    def __str__(self):
        return self.site + ' ' + str(self.num)

    def __lt__(self, other):
        if self.num == other.num:
            return self.site > other.site
        return self.num < other.num


def fun1(term1):
    flag = 0
    r_list = []
    for tester in test_list:
        if tester.level == term1:
            r_list.append(tester)
            flag = 1
    if not flag:
        print('NA')
    else:
        r_list.sort(reverse=True)
        for i in r_list:
            print(i)


def fun2(term1):
    count = 0
    count_sum = 0
    for tester in test_list:
        if tester.site == term1:
            count_sum += tester.score
            count += 1
    if count == 0:
        print('NA')
    else:
        print(f'{count} {count_sum}')


def fun3(term1):
    r_list = []
    for tester in test_list:
        if tester.date == term1:
            # 符合条件，把答案加入r_list中，如果存在+1，不存在则=1
            flag = 0
            for i in r_list:
                if i.site == tester.site:
                    i.num += 1
                    flag = 1
                    break
            if flag == 0:
                r_list.append(node2(tester.site, 1))
    r_list.sort(reverse=True)
    if len(r_list) == 0:
        print('NA')
    else:
        for i in r_list:
            print(i)


if __name__ == '__main__':
    test_list = []
    n, m = map(int, input().split())
    for i in range(n):
        a, b = input().split()
        test_list.append(node(a, b))
    # test_list.sort(reverse=True)
    for i in range(m):
        type_, term = input().split()
        print(f'Case {i+1}: {type_} {term}')
        if type_ == '1':
            fun1(term)
        elif type_ == '2':
            fun2(term)
        else:
            fun3(term)
"""
python 超时最后两个测试点过不去
c 过多了一个测试点
柳神代码全过
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
struct node{
	string t;
	int value;
}; 
bool cmp(const node &a, const node &b){
	return a.value == b.value ? a.t < b.t : a.value > b.value;
}
int main(){
	int n,m;
	vector<node> a;
	cin>>n>>m;
	for(int i=0;i<n;i++){
		node d;
		cin>>d.t>>d.value;
		a.push_back(d);
	}
	for(int i=0;i<m;i++){
		int type;string term;
		cin>>type>>term;
		vector<node> ans;
		printf("Case %d: %d %s\n",i+1,type,term.c_str());
		if(type==1){
			for(int j=0;j<n;j++){
				if(a[j].t[0] == term[0])
				ans.push_back(a[j]);
			}
		}
		else if(type==2){
			int count = 0;
			int count_sum = 0;
			for(int j=0;j<n;j++){
				if(a[j].t.substr(1,3) == term){
					count ++;
					count_sum += a[j].value;
				}
			}
			if(count==0)
				printf("NA\n");
			else
				printf("%d %d\n",count, count_sum);
		}
		else{
			for(int j=0;j<n;j++){
				if(a[j].t.substr(4,6) == term){
					string key = a[j].t.substr(1,3);
					int flag = 0;
					for(int i=0;i<ans.size();i++){
						if(ans[i].t == key){
							ans[i].value += 1;
							flag = 1;
							break;
						}
					}
					if(flag==0){
						node x;
						x.t= key;x.value=1;
						ans.push_back(x);
					}
				}
			}
		}
		sort(ans.begin(),ans.end(),cmp);
		if(ans.size() == 0 && type!=2){
			printf("NA\n");
		}
		else
		for(int i=0;i<ans.size();i++){
			printf("%s %d\n",ans[i].t.c_str(),ans[i].value);
		}
	}
	return 0;
}


#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
struct node {
    string t;
    int value;
};
bool cmp(const node &a, const node &b) {
    return a.value != b.value ? a.value > b.value : a.t < b.t;
}
int main() {
    int n, k, num;
    string s;
    cin >> n >> k;
    vector<node> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i].t >> v[i].value;
    for (int i = 1; i <= k; i++) {
        cin >> num >> s;
        printf("Case %d: %d %s\n", i, num, s.c_str());
        vector<node> ans;
        int cnt = 0, sum = 0;
        if (num == 1) {
            for (int j = 0; j < n; j++)
                if (v[j].t[0] == s[0]) ans.push_back(v[j]);
        } else if (num == 2) {
            for (int j = 0; j < n; j++) {
                if (v[j].t.substr(1, 3) == s) {
                    cnt++;
                    sum += v[j].value;
                }
            }
            if (cnt != 0) printf("%d %d\n", cnt, sum);
        } else if (num == 3) {
            unordered_map<string, int> m;
            for (int j = 0; j < n; j++)
                if (v[j].t.substr(4, 6) == s) m[v[j].t.substr(1, 3)]++;
            for (auto it : m) ans.push_back({it.first, it.second});
        }
        sort(ans.begin(), ans.end(),cmp);
        for (int j = 0; j < ans.size(); j++)
            printf("%s %d\n", ans[j].t.c_str(), ans[j].value);
        if (((num == 1 || num == 3) && ans.size() == 0) || (num == 2 && cnt == 0)) printf("NA\n");
    }
    return 0;
}
————————————————
版权声明：本文为CSDN博主「柳婼」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liuchuo/article/details/84973049
"""
