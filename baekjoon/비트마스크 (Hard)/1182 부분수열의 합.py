n, m = map(int, input().split())
a = list(map(int, input().split()))
answer = 0

# 원소가 포함되거나 포함되지 않는 경우 -> 2의 n승
# 예를 들어 00001이면 첫 번째 원소만 포함
for i in range(1, (1 << n)):
    s = 0
    for k in range(n):
        # k 번째 원소가 포함되면
        if (i & (1 << k)) > 0:
            s += a[k]
    if m == s:
        answer += 1

print(answer)