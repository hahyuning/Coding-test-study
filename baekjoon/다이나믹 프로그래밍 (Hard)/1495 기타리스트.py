n, s, m = map(int, input().split())
v = [0] + list(map(int, input().split()))

# d[i][j]: i번 곡을 볼륨 j로 연주할 수 있는지의 여부
# i - 1을 연주한 상황에서 i를 연주하는 상황 생각 (다음으로 나아가는 방법)
d = [[0] * (m + 1) for _ in range(n + 1)]
d[0][s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        if d[i - 1][j] == 0:
            continue

        if j - v[i] >= 0:
            d[i][j - v[i]] = 1
        if j + v[i] <= m:
            d[i][j + v[i]] = 1

ans = -1
for i in range(m + 1):
    if d[n][i] == 1:
        ans = i

print(ans)