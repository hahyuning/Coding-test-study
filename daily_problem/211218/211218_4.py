import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def inorder(node):
    global last

    if node.left != -1:
        inorder(tree[node.left])
    last = node.data
    if node.right != -1:
        inorder(tree[node.right])

def dfs(now, level):
    global ans
    if now == last:
        ans = level
        return

    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt, level + 1)

n = int(input())
tree = {}
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    node, left, right = map(int, input().split())
    tree[node] = Node(node, left, right)
    if left != -1:
        graph[node].append(left)
    if right != -1:
        graph[node].append(right)

visited = [False] * (n + 1)
last = -1
inorder(tree[1])
ans = -1
dfs(1, 0)
print(ans + 2 * (n - 1 - ans))