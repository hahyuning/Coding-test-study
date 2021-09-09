from itertools import product
import copy


def check(a, dir):
    # k: 위, 아래, 왼쪽, 오른쪽
    for k in dir:
        merge_check = [[False] * n for _ in range(n)]  # 칸이 합쳐진 적이 있는지 기록

        while True:
            # 더이상 이동하지 않을 때까지 반복
            move = False

            # 위로 이동하는 경우
            if k == 0:
                for i in range(1, n):
                    for j in range(n):
                        # 수가 없는 경우
                        if a[i][j] == 0:
                            continue

                        # 이동하려는 칸에 수가 없는 경우
                        if a[i - 1][j] == 0:
                            a[i - 1][j] = a[i][j]
                            merge_check[i - 1][j] = merge_check[i][j]
                            a[i][j] = 0
                            move = True
                        # 이동하려는 칸에 있는 수가 현재 수와 같은 경우
                        elif a[i - 1][j] == a[i][j]:
                            # 이전에 합쳐진 적이 없어야 함
                            if not merge_check[i - 1][j] and not merge_check[i][j]:
                                a[i - 1][j] *= 2
                                a[i][j] = 0
                                merge_check[i - 1][j] = True
                                move = True
            # 아래로 이동하는 경우
            elif k == 1:
                for i in range(n - 2, -1, -1):
                    for j in range(n):
                        # 수가 없는 경우
                        if a[i][j] == 0:
                            continue

                        # 이동하려는 칸에 수가 없는 경우
                        if a[i + 1][j] == 0:
                            a[i + 1][j] = a[i][j]
                            merge_check[i + 1][j] = merge_check[i][j]
                            a[i][j] = 0
                            move = True
                        # 이동하려는 칸에 있는 수가 현재 수와 같은 경우
                        elif a[i + 1][j] == a[i][j]:
                            # 이전에 합쳐진 적이 없어야 함
                            if not merge_check[i + 1][j] and not merge_check[i][j]:
                                a[i + 1][j] *= 2
                                a[i][j] = 0
                                merge_check[i + 1][j] = True
                                move = True
            # 왼쪽으로 이동하는 경우
            elif k == 2:
                for j in range(1, n):
                    for i in range(n):
                        # 수가 없는 경우
                        if a[i][j] == 0:
                            continue

                        # 이동하려는 칸에 수가 없는 경우
                        if a[i][j - 1] == 0:
                            a[i][j - 1] = a[i][j]
                            merge_check[i][j - 1] = merge_check[i][j]
                            a[i][j] = 0
                            move = True
                        # 이동하려는 칸에 있는 수가 현재 수와 같은 경우
                        elif a[i][j - 1] == a[i][j]:
                            # 이전에 합쳐진 적이 없어야 함
                            if not merge_check[i][j - 1] and not merge_check[i][j]:
                                a[i][j - 1] *= 2
                                a[i][j] = 0
                                merge_check[i][j - 1] = True
                                move = True
            # 오른쪽으로 이동하는 경우
            else:
                for j in range(n - 2, -1, -1):
                    for i in range(n):
                        # 수가 없는 경우
                        if a[i][j] == 0:
                            continue

                        # 이동하려는 칸에 수가 없는 경우
                        if a[i][j + 1] == 0:
                            a[i][j + 1] = a[i][j]
                            merge_check[i][j + 1] = merge_check[i][j]
                            a[i][j] = 0
                            move = True
                        # 이동하려는 칸에 있는 수가 현재 수와 같은 경우
                        elif a[i][j + 1] == a[i][j]:
                            # 이전에 합쳐진 적이 없어야 함
                            if not merge_check[i][j + 1] and not merge_check[i][j]:
                                a[i][j + 1] *= 2
                                a[i][j] = 0
                                merge_check[i][j + 1] = True
                                move = True
            if not move:
                break

    res = max([max(row) for row in a])
    return res


# ------------------------------------------------------------
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = -1
for dir in product([0, 1, 2, 3], repeat=5):
    a = copy.deepcopy(board)
    res = check(a, dir)
    ans = max(ans, res)
print(ans)