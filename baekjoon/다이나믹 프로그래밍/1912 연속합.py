n = int(input())
a = list(map(int, input().split()))
# d[i] : i번째 수로 끝나는 가장 큰 연속합
# d[i] = max(a[i], d[i - 1] + a[i])
# 정답 = max(d)
d = [0] * n

for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if a[i] < d[i - 1] + a[i]:
        d[i] = d[i - 1] + a[i]

print(max(d))