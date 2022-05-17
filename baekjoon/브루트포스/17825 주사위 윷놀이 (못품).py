board = [
    0, 2, 4, 6, 8,
    10, 13, 16, 19, 25,
    12, 14, 16, 18, 20,
    22, 24, 22, 24, 26,
    28, 26, 27, 28, 30,
    32, 34, 36, 38, 30,
    35, 40, 0
]

intersection = []
for i in range(len(board)):
    if i == 5:
        intersection.append([6, 10])
    elif i == 9:
        intersection.append([29, 29])
    elif i == 14:
        intersection.append([15, 17])
    elif i == 16:
        intersection.append([9, 9])
    elif i == 20:
        intersection.append([24, 24])
    elif i == 21:
        intersection.append([9, 9])
    elif i == 22:
        intersection.append([21, 21])
    elif i == 23:
        intersection.append([22, 22])
    elif i == 24:
        intersection.append([23, 25])
    elif i == 28:
        intersection.append([31, 31])
    elif i == 32:
        intersection.append([32, 32])
    else:
        intersection.append([i + 1, i + 1])


def find_nxt(s, k):
    now = s
    for i in range(k):
        if i == 0:
            now = intersection[now][0]
        else:
            now = intersection[now][1]
    return now


def solution(cnt, location, score):
    if cnt == 10:
        return score

    ans = 0
    for i in range(4):
        nxt = find_nxt(location[i], dice[cnt])

        check = True
        if nxt != 32:
            for j in range(4):
                if i != j and nxt == location[j]:
                    check = False

        if check:
            nxt_location = location[:]
            nxt_location[i] = nxt
            tmp = solution(cnt + 1, nxt_location, score + board[nxt])
            ans = max(tmp, ans)

    return ans


if __name__ == '__main__':
    dice = list(map(int, input().split()))
    print(solution(0, [0, 0, 0, 0], 0))