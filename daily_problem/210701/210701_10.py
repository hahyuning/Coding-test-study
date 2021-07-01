import sys
input = sys.stdin.readline

s, e, q = input().split()
s = list(map(int, s.split(":")))
e = list(map(int, e.split(":")))
q = list(map(int, q.split(":")))
s_time = s[0] * 60 + s[1]
e_time = e[0] * 60 + e[1]
q_time = q[0] * 60 + q[1]

ans = dict()
while True:
    x = input().rstrip()
    if not x:
        break
    t, x = x.split()
    t = list(map(int, t.split(":")))
    time = t[0] * 60 + t[1]
    if time <= s_time:
        if x in ans:
            continue
        ans[x] = 1
    elif e_time <= time <= q_time:
        if x not in ans:
            continue
        ans[x] = 0

cnt = 0
for i, x in ans.items():
    if x == 0:
        cnt += 1
print(cnt)

