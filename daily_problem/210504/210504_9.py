import sys
input = sys.stdin.readline

n = int(input())
first = dict()

a, b, c, d = [], [], [], []
for _ in range(n):
    aa, bb, cc, dd = map(int, input().split())
    a.append(aa)
    b.append(bb)
    c.append(cc)
    d.append(dd)


for aaa in a:
    for bbb in b:
        first[aaa + bbb] = first.get(aaa + bbb, 0) + 1

answer = 0
for ccc in c:
    for ddd in d:
        answer += first.get(-(ccc + ddd), 0)

print(answer)