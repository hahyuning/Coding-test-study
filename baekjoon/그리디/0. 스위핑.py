import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    s, e = map(int, input().split())
    a.append((s, e))
a.sort()

ans = 0
lt = a[0][0]
rt = a[0][1]

for i in range(1, n):
    # 현재 구간과 이번 선분이 합쳐질 수 없는 경우
    if rt < a[i][0]:
        ans += (rt - lt)

        lt = a[i][0]
        rt = a[i][1]
    else:
        rt = max(rt, a[i][1])

ans += (rt - lt)
print(ans)