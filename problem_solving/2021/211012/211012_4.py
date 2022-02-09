def check(idx, s, max_jump):
    global ans

    if idx == n - 1:
        if ans == -1 or s < ans:
            ans = s
        return

    # 일반 점프
    if idx + 1 < n:
        check(idx + 1, s + jump[idx][0], max_jump)
    # 큰 점프
    if idx + 2 < n:
        check(idx + 2, s + jump[idx][1], max_jump)
    # 매우 큰 점프
    if idx + 3 < n and not max_jump:
        check(idx + 3, s + k, True)


n = int(input())
jump = []
for _ in range(n - 1):
    x, y = map(int, input().split())
    jump.append((x, y))
k = int(input())

ans = -1
check(0, 0, False)
print(ans)