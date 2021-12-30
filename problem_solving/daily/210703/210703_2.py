import sys

def solution(cnt, r, g, b, idx):

    global min_diff
    if cnt > 7:
        return
    if idx >= n:
        if cnt > 1:
            diff = abs(r // cnt - gom_r) + abs(g // cnt - gom_g) + abs(b // cnt - gom_b)
            min_diff = min(min_diff, diff)
        return

    solution(cnt + 1, r + color[idx][0], g + color[idx][1], b + color[idx][2], idx + 1)
    solution(cnt, r, g, b, idx + 1)


n = int(input())
color = []
for _ in range(n):
    r, g, b = map(int, input().split())
    color.append((r, g, b))
gom_r, gom_g, gom_b = map(int, input().split())
min_diff = sys.maxsize
solution(0, 0, 0, 0, 0)
print(min_diff)