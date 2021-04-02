n, m, k = map(int, input().split()) # n x m 행렬에서 k개의 수를 뽑아 합 최대로 만들기
num_list = [list(map(int, input().split())) for _ in range(n)] # 숫자 리스트
check_list = [[False] * m for _ in range(n)] # 숫자를 사용했는지의 여부를 저장할 리스트
ans = -2147483647 # 최대값 초기화
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(px, py, cnt, sum):
    global ans

    # 종료 조건 : 뽑힌 수의 개수가 k개가 되면 정료
    if cnt == k:
        # ans를 최대값으로 변경
        ans = max(ans, sum)
        return

    for x in range(px, n):
        # x의 좌표가 px이면 py부터 시작, 아니면 0부터 시작
        for y in range(py if x == px else 0, m):
            # 수 사용여부 확인
            if check_list[x][y]:
                continue

            # 인접한 영역을 선택했는지 확인
            ok = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if check_list[nx][ny]:
                        ok = False

            # 인접한 영역을 선택하지 않았다면
            if ok:
                check_list[x][y] = True
                dfs(x, y, cnt + 1, sum + num_list[x][y])
                check_list[x][y] = False

dfs(0, 0, 0, 0)
print(ans)
