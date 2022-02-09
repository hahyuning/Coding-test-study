n = int(input())
m = int(input())
wall = [True] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(a, b):
        wall[i] = False

print(sum(wall[1:n + 1]))
