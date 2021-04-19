n = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:
    scv.append(0)

# d[i][j][k]: scv의 체력이 i, j, k 일 때 모두 파괴하는 최소 공격 횟수
# 인덱스가 음수인 경우가 많이 발생하므로 탑다운 방식 사용
d = [[[-1] * 61 for _ in range(61)] for _ in range(61)]

def top_down(i, j, k):
    # 범위 검사
    if i < 0:
        return top_down(0, j, k)
    if j < 0:
        return top_down(i, 0, k)
    if k < 0:
        return top_down(i, j, 0)

    # 모두 파괴되었으므로 0 반환
    if i == j == k == 0:
        return 0

    if d[i][j][k] != -1:
        return d[i][j][k]

    ans = 10000000
    if ans > top_down(i - 1, j - 3, k - 9):
        ans = top_down(i - 1, j - 3, k - 9)
    if ans > top_down(i - 1, j - 9, k - 3):
        ans = top_down(i - 1, j - 9, k - 3)
    if ans > top_down(i - 3, j - 1, k - 9):
        ans = top_down(i - 3, j - 1, k - 9)
    if ans > top_down(i - 3, j - 9, k - 1):
        ans = top_down(i - 3, j - 9, k - 1)
    if ans > top_down(i - 9, j - 1, k - 3):
        ans = top_down(i - 9, j - 1, k - 3)
    if ans > top_down(i - 9, j - 3, k - 1):
        ans = top_down(i - 9, j - 3, k - 1)

    d[i][j][k] = ans + 1
    return d[i][j][k]

print(top_down(scv[0], scv[1], scv[2]))