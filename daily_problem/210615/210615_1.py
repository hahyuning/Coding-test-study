# 놓인 접시의 수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a += a[:k]
keys = dict()
for x in a:
    keys[x] = 0
if c not in keys:
    keys[c] = 0

# 연속해서 먹은 초밥의 수
cnt = 0
# 먹은 초밥의 종류
kind = 0
# 최종 정답
ans = 0
lt = 0
rt = 0
while lt < len(a) and rt < len(a):
    # 연속해서 먹은 개수가 k개 이상인 경우 -> lt 증가
    if cnt >= k:
        keys[a[lt]] -= 1
        if keys[a[lt]] == 0:
            kind -= 1
        lt += 1
        cnt -= 1
    # 연속해서 먹은 개수가 k개 미만인 경우 -> rt 증가
    else:
        if keys[a[rt]] == 0:
            kind += 1
        keys[a[rt]] += 1
        rt += 1
        cnt += 1

    # 정답 갱신
    if kind >= ans:
        ans = kind
        # 만약 먹은 초밥 중에 쿠폰 초밥이 없는 경우
        if keys[c] == 0:
            ans += 1

print(ans)