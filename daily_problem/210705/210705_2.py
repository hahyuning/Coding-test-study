from collections import deque

n, k = map(int, input().split())
a = []
for _ in range(2):
    b = input()
    a.append(b)

q = deque()
q.append((0, 0, 1))

check = [[False] * n for _ in range(2)]
check[0][0] = True

while q:
    x, now, remove = q.popleft()
    if remove <= now + 1:
        if now + 1 >= n:
            print(1)
            break
        if not check[x][now + 1] and a[x][now + 1] == "1":
            check[x][now + 1] = True
            q.append((x, now + 1, remove + 1))

    if remove <= now - 1:
        if now - 1 >= n:
            print(1)
            break
        if not check[x][now - 1] and a[x][now - 1] == "1":
            check[x][now - 1] = True
            q.append((x, now - 1, remove + 1))

    if remove <= now + k:
        if now + k >= n:
            print(1)
            break
        if not check[1 - x][now + k] and a[1 - x][now + k] == "1":
            check[1 - x][now + k] = True
            q.append((1 - x, now + k, remove + 1))
else:
    print(0)

