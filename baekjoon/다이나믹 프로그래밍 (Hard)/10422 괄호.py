t = int(input())

# d[i]: 길이가 i인 올바른 괄호 문자열의 개수
# d[i] = sum(d[j - 2] * d[i - j]), 2 <= j <= n, j는 짝수
d = [0] * 5001
d[0] = 1

for i in range(1, 5001):
    for j in range(2, i + 1, 2):
        d[i] += d[j - 2] * d[i - j]

for _ in range(t):
    n = int(input())
    print(d[n] % 1000000007)