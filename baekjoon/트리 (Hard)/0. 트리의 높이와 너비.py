def inorder(root, level):
    global num
    if a[root][0] != -1:
        inorder(a[root][0], level + 1)

    row[level].append(num)
    num += 1

    if a[root][1] != -1:
        inorder(a[root][1], level + 1)


n = int(input())
a = [[0] * 2 for _ in range(n + 1)]
node = [0 for _ in range(n + 1)]
row = [[] for _ in range(n + 1)]
num = 1

for _ in range(n):
    x, l, r = map(int, input().split())
    a[x][0] = l
    a[x][1] = r

    node[x] += 1
    if l != -1:
        node[l] += 1
    if r != -1:
        node[r] += 1

root = 0
for i in range(1, n + 1):
    if node[i] == 1:
        root = i

inorder(root, 1)
res = max(row[1]) - min(row[1]) + 1
level = 1
for i in range(2, n + 1):
    if row[i]:
        if res < max(row[i]) - min(row[i]) + 1:
            res = max(row[i]) - min(row[i]) + 1
            level = i
print(level, res)