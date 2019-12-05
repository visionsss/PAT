def lca(inl, inr, pre_root, a, b):
    if inl > inr:
        return
    inRoot = pos[pre_order[pre_root]]
    aIn = pos[a]
    bIn = pos[b]
    if aIn < inRoot and bIn < inRoot:
        lca(inl, inRoot-1, pre_root+1, a, b)
    elif (aIn < inRoot < bIn) or (aIn > inRoot > bIn):
        print(f"LCA of {a} and {b} is {in_order[inRoot]}.")
    elif aIn > inRoot and bIn > inRoot:
        lca(inRoot + 1, inr, pre_root + 1 + (inRoot - inl), a, b)
    elif aIn == inRoot:
        print(f"{a} is an ancestor of {b}.")
    elif bIn == inRoot:
        print(f"{b} is an ancestor of {a}.")


if __name__ == '__main__':
    n, m = map(int, input().split())
    in_order = list(map(int, input().split()))
    pre_order = list(map(int, input().split()))
    pos = {}
    for i in range(len(in_order)):
        pos[in_order[i]] = i
    for i in range(n):
        n1, n2 = map(int, input().split())
        if n1 not in in_order and n2 not in in_order:
            print(f'ERROR: {n1} and {n2} are not found.')
        elif n1 not in in_order:
            print(f'ERROR: {n1} is not found.')
        elif n2 not in in_order:
            print(f'ERROR: {n2} is not found.')
        else:
            lca(0, m-1, 0, n1, n2)

"""
 
#include <iostream>
#include <vector>
#include <map>
using namespace std;
map<int, int> pos;
vector<int> in, pre;
void lca(int inl, int inr, int preRoot, int a, int b) {
    if (inl > inr) return;
    int inRoot = pos[pre[preRoot]], aIn = pos[a], bIn = pos[b];
    if (aIn < inRoot && bIn < inRoot)
        lca(inl, inRoot-1, preRoot+1, a, b);
    else if ((aIn < inRoot && bIn > inRoot) || (aIn > inRoot && bIn < inRoot))
        printf("LCA of %d and %d is %d.\n", a, b, in[inRoot]);
    else if (aIn > inRoot && bIn > inRoot)
        lca(inRoot+1, inr, preRoot+1+(inRoot-inl), a, b);
    else if (aIn == inRoot)
            printf("%d is an ancestor of %d.\n", a, b);
    else if (bIn == inRoot)
            printf("%d is an ancestor of %d.\n", b, a);
}
int main() {
    int m, n, a, b;
    scanf("%d %d", &m, &n);
    in.resize(n + 1), pre.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &in[i]);
        pos[in[i]] = i;
    }
    for (int i = 1; i <= n; i++) scanf("%d", &pre[i]);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &a, &b);
        if (pos[a] == 0 && pos[b] == 0)
            printf("ERROR: %d and %d are not found.\n", a, b);
        else if (pos[a] == 0 || pos[b] == 0)
            printf("ERROR: %d is not found.\n", pos[a] == 0 ? a : b);
        else
            lca(1, n, 1, a, b);
    }
    return 0;
}
————————————————
版权声明：本文为CSDN博主「柳婼」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liuchuo/article/details/82560863
 # 只过了2个测试点
import copy
class Tree:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


def get_tree(in_, pre_, p):
    if len(in_) == 1:
        return Tree(key=in_[0], parent=p)
    if len(in_) == 0:
        return None
    mid_ = in_.index(pre_[0])
    kid = Tree(pre_[0])
    kid.left = get_tree(in_[:mid_], pre_[1:1 + len(in_[:mid_])], p)
    kid.right = get_tree(in_[mid_ + 1:], pre_[mid_ + 1:], p)
    return kid


def traversal(xx, key):
    # print(xx.key, answer_list)
    if f == 1:
        return
    global a_list
    if xx.key == key:
        a_list = copy.deepcopy(answer_list)
        return a_list
    if xx.right is not None and flag[in_order.index(xx.key)] == 0:
        answer_list.append(xx.key)
        traversal(xx.right, key)

    if xx.left is not None and flag[in_order.index(xx.key)] == 0:
        answer_list.append(xx.key)
        traversal(xx.left, key)

    if xx.right is None or xx.left is None:
        answer_list.pop(-1)
        flag[in_order.index(xx.key)] = 1




if __name__ == '__main__':
    m, n = map(int, input().split())
    in_order = list(map(int, input().split()))
    pre_order = list(map(int, input().split()))
    # Build_Tree
    T = Tree(pre_order[0])
    mid = in_order.index(pre_order[0])
    T.left = get_tree(in_order[:mid], pre_order[1:1+len(in_order[:mid])], T)
    T.right = get_tree(in_order[mid+1:], pre_order[mid+1:], T)
    for i in range(m):
        n1, n2 = map(int, input().split())
        if n1 not in in_order and n2 not in in_order:
            print(f'ERROR: {n1} and {n2} are not found.')
        elif n1 not in in_order:
            print(f'ERROR: {n1} is not found.')
        elif n2 not in in_order:
            print(f'ERROR: {n2} is not found.')
        else:
            flag = [0 for kkk in range(len(in_order))]
            answer_list = []
            a_list = []
            f = 0
            traversal(T, n1)
            list1 = a_list
            flag = [0 for kkk in range(len(in_order))]
            answer_list = []
            a_list = []
            f = 0
            traversal(T, n2)
            list2 = a_list
            if n1 in list2:
                print(f'{n1} is an ancestor of {n2}.')
            elif n2 in list1:
                print(f'{n2} is an ancestor of {n1}.')
            else:
                for ii in list2[::-1]:
                    if ii in list1:
                        print(f'LCA of {n1} and {n2} is {ii}.')
                        break
"""