n, k = map(int, input().split())
a = list(map(int, input().split()))

# 연속 부분 수열에 포함된 각 숫자의 개수를 저장할 배열
cnt = [0] * 100001
lt = 0
rt = 0
ans = 0
while lt <= rt and rt < n:
    while rt < n and cnt[a[rt]] <= k:
        if cnt[a[rt]] == k:
            break
        cnt[a[rt]] += 1
        ans = max(ans, rt - lt + 1)
        rt += 1

    while lt < rt:
        if cnt[a[lt]] == k:
            cnt[a[lt]] -= 1
            lt += 1
            break
        cnt[a[lt]] -= 1
        lt += 1
print(ans)
