n = int(input())
w = [0] + [int(input()) for _ in range(n)]

# d[i]: i번째 포도주까지 고려했을 때 최대로 마신 포도주의 양
# d[i] = max(d[i - 3] + w[i] + w[i - 1], d[i - 2] + w[i], d[i - 1])
# 1번 상황: i - 2 마시지 않고 i - 1, i 마시는 경우
# 2번 상황: i - 1 마시지 않고 i 마시는 경우
# 3번 상황: i 마시지 않는 경우
d = [0] * (n + 1)

if n < 3:
    print(sum(w))
else:
    d[1] = w[1]
    d[2] = w[1] + w[2]
    for i in range(3, n + 1):
        d[i] = max(d[i - 3] + w[i] + w[i - 1], d[i - 2] + w[i], d[i - 1])
    print(d[n])

