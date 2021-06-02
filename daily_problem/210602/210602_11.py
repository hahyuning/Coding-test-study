import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()
for i in range(1, n + 1):
    s = input().rstrip()
    dic[str(i)] = s
    dic[s] = i

for _ in range(m):
    t = input().rstrip()
    print(dic[t])

