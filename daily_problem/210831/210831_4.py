n, k = map(int, input().split())
a = list(map(int, input().split()))

diff = []
for i in range(n - 1):
    diff.append(a[i + 1] - a[i])
diff.sort()

print(sum(diff[:n - k]))