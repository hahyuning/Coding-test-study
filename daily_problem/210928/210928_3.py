n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

start = a[0]
end = a[0] + l
ans = 1

for i in range(n):
    if start <= a[i] < end:
        continue

    start = a[i]
    end = a[i] + l
    ans += 1
print(ans)