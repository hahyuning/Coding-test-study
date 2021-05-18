# 세대만큼 드래곤 커브를 만드는 함수
def dragon_curve(d, g):
    ans = [d]
    for k in range(1, g + 1):
        # 이전까지의 드래곤 커브를 뒤집어서 1씩 더하기
        tmp = ans[:]
        tmp = tmp[::-1]
        for i in range(len(tmp)):
            tmp[i] = (tmp[i] + 1) % 4
        ans += tmp
    return ans

n = int(input())
# x, y, d, g: 드래곤 커브의 시작 위치, 시작 방향, 세대
# 방향: 동북서남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

check = [[0] * 101 for _ in range(101)]
for _ in range(n):
    y, x, d, g = map(int, input().split())
    check[x][y] = 1
    curve = dragon_curve(d, g)

    for k in curve:
        x += dx[k]
        y += dy[k]
        check[x][y] = 1

ans = 0
# 드래곤 커브의 일부인 것 확인
for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i + 1][j] == 1 and check[i][j + 1] == 1 and check[i + 1][j + 1] == 1:
            ans += 1
print(ans)
