import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
words = dict()
for _ in range(n):
    x = input()
    words[x] = 1
ans = 0
for _ in range(m):
    x = input()
    if x in words:
        ans += 1
print(ans)