n, m = map(int, input().split())
h = [0] + list(map(int, input().split()))
arr = [0] * (n + 2)

for _ in range(m):
    a, b, k = map(int, input().split())
    arr[a] += k
    arr[b + 1] -= k

s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + arr[i]

for i in range(1, n + 1):
    s[i] += h[i]
print(*s[1:])