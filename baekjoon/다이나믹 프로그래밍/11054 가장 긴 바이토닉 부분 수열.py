n = int(input())
a = list(map(int, input().split()))
# d[i] : a[i]에서 끝나는 가장 긴 증가하는 부분 수열의 길이
d = [1] * n
# e[i] : a[i]에서 시작하는 가장 긴 감소하는 부분 수열의 길이
e = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j] + 1)

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            e[i] = max(e[i], e[j] + 1)

answer = 0
for x, y in zip(d, e):
    answer = max(answer, x + y - 1)

print(answer)