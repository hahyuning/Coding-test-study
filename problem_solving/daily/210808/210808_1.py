n, m, k = map(int, input().split())
# 전체: C(n, m)
# 경우의 수: C(m, 0) * C(n - m, m - k) + C(m, 1) * C(n - m, m - k - 1) + ... + C(m, k) * C(n - m, 0)

factorial = [1] * (n + 1)
for i in range(2, n + 1):
    factorial[i] = factorial[i - 1] * i

all_cnt = factorial[n] / (factorial[m] * factorial[n - m])
cnt = 0
for i in range(k, m + 1):
    if n - m >= m - i:
        cnt += (factorial[n - m] / (factorial[m - i] * factorial[n - 2 * m + i])) * (factorial[m] / (factorial[i] * factorial[m - i]))
print(cnt / all_cnt)
