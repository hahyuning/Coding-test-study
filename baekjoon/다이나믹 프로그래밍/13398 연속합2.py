n = int(input())
a = list(map(int, input().split()))
# d[i] : a[i]에서 끝나는 최대 연속합
d = [0] * n
# e[i] : a[i]에서 시작하는 최대 연속합
e = [0] * n

for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue

    d[i] = max(d[i], d[i - 1] + a[i])

for i in range(n - 1, -1, -1):
    e[i] = a[i]
    if i == n - 1:
        continue

    e[i] = max(e[i], e[i + 1] + a[i])

# 제거 안한 경우와 비교
# 0번재와 n - 1번째는 비교하지 않아도 된다
answer = max(d)
for i in range(1, n - 1):
    answer = max(answer, d[i - 1] + e[i + 1])
print(answer)