def make_tree(arr, x):
    mid = len(arr) // 2
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    make_tree(arr[:mid], x + 1)
    make_tree(arr[mid + 1:], x + 1)

k = int(input())
order = list(map(int, input().split()))
tree = [[] for _ in range(k)]

make_tree(order, 0)
for i in range(k):
    print(*tree[i])