n = int(input())
tree = [[-1] * 2 for _ in range(n + 1)]
for i in range(1, n + 1):
    a, b = map(int, input().split())
    tree[i][0] = a
    tree[i][1] = b

m = int(input())
now = 1

while True:
    if tree[now][0] == -1 and tree[now][1] == -1:
        break

    elif tree[now][0] == -1:
        now = tree[now][1]
    elif tree[now][1] == -1:
        now = tree[now][0]

    elif m % 2 == 1:
        now = tree[now][0]
        m = m // 2 + 1
    else:
        now = tree[now][1]
        m = m // 2

print(now)