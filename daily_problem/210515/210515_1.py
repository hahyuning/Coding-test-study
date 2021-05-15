n = int(input())
study = []
for _ in range(n):
    s, e = map(int, input().split())
    study.append((s, e))

study.sort()
ans = 1
last_time = study[0][1]

for i in range(1, n):
    if last_time > study[i][0]:
        ans += 1
    last_time = max(last_time, study[i][1])
print(ans)
