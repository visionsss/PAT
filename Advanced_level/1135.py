class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def build(root_, key):
    if root_ is None:
        root_ = Node(key=key)
    elif abs(key) <= abs(root_.key):
        root_.left = build(root_.left, key=key)
    else:
        root_.right = build(root_.right, key=key)
    return root_


def judge1(root_):
    if not root_:
        return True
    if root_.key < 0:
        if root_.left is not None:
            if root_.left.key < 0:
                return False
        if root_.right is not None:
            if root_.right.key < 0:
                return False
    return judge1(root_.left) and judge1(root_.right)


def get_num(root_):
    if root_ is None:
        return 0
    else:
        r = get_num(root_.right)
        l = get_num(root_.left)
        if root_.key > 0:
            return max(r, l) + 1
        else:
            return max(r, l)


def judge2(root_):
    if root_ is None:
        return True
    l = get_num(root_.left)
    r = get_num(root_.right)
    if l != r:
        return False
    return judge2(root_.right) and judge2(root_.left)


if __name__ == '__main__':
    k = int(input())
    for kk in range(k):
        n = int(input())
        pre_order = list(map(int, input().split()))
        root = None
        for i in pre_order:
            root = build(root, i)
        if pre_order[0] < 0 or judge1(root) is False or judge2(root) is False:
            print('No')
        else:
            print('Yes')
