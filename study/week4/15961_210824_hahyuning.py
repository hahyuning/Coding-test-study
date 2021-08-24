# 놓인 접시의 수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a += a[:k]
keys = dict()
for x in a:
    keys[x] = 0
if c not in keys:
    keys[c] = 0

cnt = 0
kind = 0
ans = 0
lt = 0
rt = 0
while lt < len(a) and rt < len(a):
    if cnt >= k:
        keys[a[lt]] -= 1
        if keys[a[lt]] == 0:
            kind -= 1
        lt += 1
        cnt -= 1
    else:
        if keys[a[rt]] == 0:
            kind += 1
        keys[a[rt]] += 1
        rt += 1
        cnt += 1

    if kind >= ans:
        ans = kind
        if keys[c] == 0:
            ans += 1

print(ans)