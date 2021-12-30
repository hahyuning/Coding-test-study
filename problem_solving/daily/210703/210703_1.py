def solution(s, cnt):
    global ans

    if s < 500:
        return
    if cnt == n:
        ans += 1
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            solution(s + a[i] - k, cnt + 1)
            check[i] = False


n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
check = [False] * n
solution(500, 0)
print(ans)