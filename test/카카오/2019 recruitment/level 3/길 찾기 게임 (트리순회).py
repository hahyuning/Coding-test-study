import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, key):
        self.x = x
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
        self.pre_result = list()
        self.post_result = list()

    def insert(self, x, key):
        current_node = self.head
        if self.head is None:
            self.head = Node(x, key)
        else:
            while True:
                if current_node.x > x:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(x, key)
                        break
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(x, key)
                        break

    def preorder(self):
        def _preorder(root):
            if root is None:
                pass
            else:
                self.pre_result.append(root.key)
                _preorder(root.left)
                _preorder(root.right)
        _preorder(self.head)

    def postorder(self):
        def _postorder(root):
            if root is None:
                pass
            else:
                _postorder(root.left)
                _postorder(root.right)
                self.post_result.append(root.key)
        _postorder(self.head)

def solution(nodeinfo):
    n = len(nodeinfo)
    # 트리 레벨의 오름차순으로 정렬
    tmp = sorted(nodeinfo, key=lambda x: x[1], reverse=True)

    T = Tree()
    for i in range(n):
        # 루트노드부터 리프노드까지 입력
        T.insert(tmp[i][0], nodeinfo.index(tmp[i]) + 1)

    T.preorder()
    T.postorder()
    return [T.pre_result, T.post_result]