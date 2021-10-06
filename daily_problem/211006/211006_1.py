def solution(row, col, idx):
    if idx == len(target):
        return 1

    if d[row][col][idx] != -1:
        return d[row][col][idx]

    ans = 0
    for i in range(col, len(stone[0])):
        if stone[1 - row][i] == target[idx]:
            ans += solution(1 - row, i + 1, idx + 1)

    d[row][col][idx] = ans
    return d[row][col][idx]

target = input()
stone = [input() for _ in range(2)]
d = [[[-1] * len(target) for _ in range(len(stone[0]) + 1)] for _ in range(2)]

print(solution(0, 0, 0) + solution(1, 0, 0))