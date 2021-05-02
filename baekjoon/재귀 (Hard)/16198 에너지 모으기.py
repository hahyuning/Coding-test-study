def energy(w, sum):
    global ans
    # 종료 조건: 남은 에너지가 2개인 경우
    if len(w) == 2:
        ans = max(ans, sum)
        return

    for i in range(1, len(w) - 1):
        energy(w[:i] + w[i + 1:], sum + w[i - 1] * w[i + 1])

# ----------------------------------------------------
n = int(input())
w = list(map(int, input().split()))

ans = 0
energy(w, 0)
print(ans)