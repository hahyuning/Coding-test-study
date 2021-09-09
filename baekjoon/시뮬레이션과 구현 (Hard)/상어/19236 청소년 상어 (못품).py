from copy import deepcopy

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def move(fish_num, fish_dir, sx, sy, s_dir):
    # 작은 번호의 물고기부터 순서대로 이동
    for fish in range(1, 17):
        # 물고기 이동 여부 체크
        fish_move = False
        for i in range(4):
            for j in range(4):
                if fish_num[i][j] == fish:
                    for k in range(8):
                        nx = i + dx[fish_dir[i][j]]
                        ny = j + dy[fish_dir[i][j]]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            # 이동하려는 칸에 상어가 없는 경우 두 칸 교환
                            if (nx, ny) != (sx, sy):
                                fish_num[i][j], fish_num[nx][ny] = fish_num[nx][ny], fish_num[i][j]
                                fish_dir[i][j], fish_dir[nx][ny] = fish_dir[nx][ny], fish_dir[i][j]
                                fish_move = True
                                break
                            else:
                                # 물고기 회전
                                fish_dir[i][j] = (fish_dir[i][j] + 1) % 8
                if fish_move == True:
                    break
            if fish_move == True:
                break

    # 상어 이동 (어려움....)
    ans = 0
    nx = sx + dx[s_dir]
    ny = sy + dy[s_dir]
    while 0 <= nx < 4 and 0 <= ny < 4:
        # 물고기를 발견한 경우
        if fish_num[nx][ny] != 0:
            tmp = fish_num[nx][ny]
            fish_num[nx][ny] = 0
            res = tmp + move(deepcopy(fish_num), deepcopy(fish_dir), nx, ny, fish_dir[nx][ny])
            ans = max(ans, res)

            fish_num[nx][ny] = tmp
        nx += dx[s_dir]
        ny += dy[s_dir]
    return ans

# 각 칸에 있는 물고기의 번호 저장
fish_num = [[0] * 4 for _ in range(4)]
# 각 칸에 있는 물고기의 방향 저장
fish_dir = [[0] * 4 for _ in range(4)]

for i in range(4):
    a = list(map(int, input().split()))
    for j in range(4):
        fish_num[i][j] = a[2 * j]
        fish_dir[i][j] = (a[2 * j + 1] - 1)

ans = fish_num[0][0]
fish_num[0][0] = 0
ans += move(fish_num, fish_dir, 0, 0, fish_dir[0][0])
print(ans)