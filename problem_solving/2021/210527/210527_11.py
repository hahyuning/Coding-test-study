class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 전위 순회
def preorder(node):
    print(node.data, end="")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])

# 중위 순회
def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.data, end="")
    if node.right != ".":
        inorder(tree[node.right])

# 후위 순회
def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.data, end="")

n = int(input())
tree = {}
for _ in range(n):
    node, left, right = input().split()
    tree[node] = Node(node, left, right)

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])