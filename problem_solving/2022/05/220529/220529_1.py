from collections import defaultdict, deque

x, y, z = map(int, input().split())
q = deque()
q.append((0, 0, z))

check = defaultdict(int)
check[(0, 0, z)] = z

while q:
    a, b, c = q.popleft()

    if a != 0:
        # x -> y
        if a <= y - b and (0, b + a, c) not in check:
            q.append((0, b + a, c))
            check[(0, b + a, c)] = c

        if a > y - b and (a - y + b, y, c) not in check:
            q.append((a - y + b, y, c))
            check[(a - y + b, y, c)] = c

        # x -> z
        if a <= z - c and (0, b, c + a) not in check:
            q.append((0, b, c + a))
            check[(0, b, c + a)] = c + a

        if a > z - c and (a - z + c, b, z) not in check:
            q.append((a - z + c, b, z))
            check[(a - z + c, b, z)] = z

    if b != 0:
        # y -> x
        if b <= x - a and (a + b, 0, c) not in check:
            q.append((a + b, 0, c))
            check[(a + b, 0, c)] = c

        if b > x - a and (x, b - x + a, c) not in check:
            q.append((x, b - x + a, c))
            check[(x, b - x + a, c)] = c

        # y -> z
        if b <= z - c and (a, 0, c + b) not in check:
            q.append((a, 0, c + b))
            check[(a, 0, c + b)] = c + b

        if b > z - c and (a, b - z + c, z) not in check:
            q.append((a, b - z + c, z))
            check[(a, b - z + c, z)] = z

    if c != 0:
        # z -> x
        if c <= x - a and (a + c, b, 0) not in check:
            q.append((a + c, b, 0))
            check[(a + c, b, 0)] = 0

        if c > x - a and (x, b, c - x + a) not in check:
            q.append((x, b, c - x + a))
            check[(x, b, c - x + a)] = c - x + a

        # z -> y
        if c <= y - b and (a, b + c, 0) not in check:
            q.append((a, b + c, 0))
            check[(a, b + c, 0)] = 0

        if c > y - b and (a, y, c - y + b) not in check:
            q.append((a, y, c - y + b))
            check[(a, y, c - y + b)] = c - y + b

ans = []
for a, b, c in check:
    if a == 0:
        if c not in ans:
            ans.append(c)

ans.sort()
print(*ans)