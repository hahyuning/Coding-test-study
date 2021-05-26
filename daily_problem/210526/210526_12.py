from collections import deque
n = int(input())
a = list(map(int, input().split()))
ballons = deque()
for i, x in enumerate(a, start=1):
    ballons.append((x, i))

ans = []
while len(ballons) > 1:
    x, i = ballons.popleft()
    ans.append(i)
    if x > 0:
        for _ in range(x - 1):
            tmp = ballons.popleft()
            ballons.append((tmp[0], tmp[1]))
    else:
        for _ in range(-x):
            tmp = ballons.pop()
            ballons.appendleft((tmp[0], tmp[1]))
ans.append(ballons[0][1])
print(*ans)