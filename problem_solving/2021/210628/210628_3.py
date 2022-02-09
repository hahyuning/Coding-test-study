from bisect import bisect_left
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name = []
score = []
for _ in range(n):
    a, b = input().restrip().split()
    name.append(a)
    score.append(int(b))
for _ in range(m):
    k = int(input())
    i = bisect_left(score, k)
    print(name[i])
