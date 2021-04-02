import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 1000001


for i in range(2, 1000001):
    j = 1
    while i * j <= 1000000:
        dp[i * j] += i
        j += 1

s = [0] * 1000001
for i in range(1, 1000001):
    s[i] = s[i - 1] + dp[i]

for _ in range(n):
    print(s[int(input())])