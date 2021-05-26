left = ["qwert ", "asdfg ", "zxcv  "]
right = [" yuiop", " hjkl ", "bnm   "]

lx, ly = -1, -1
rx, ry = -1, -1

a, b = input().split()
for i in range(3):
    for j in range(6):
        if left[i][j] == a:
            lx, ly = i, j
        if right[i][j] == b:
            rx, ry = i, j

string = input()
ans = 0
for c in string:
    for i in range(3):
        for j in range(6):
            if c == left[i][j]:
                ans += abs(i - lx) + abs(j - ly) + 1
                lx, ly = i, j
            if c == right[i][j]:
                ans += abs(i - rx) + abs(j - ry) + 1
                rx, ry = i, j

print(ans)