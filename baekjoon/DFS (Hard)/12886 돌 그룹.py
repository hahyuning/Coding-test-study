import sys
sys.setrecursionlimit(1500 * 1500)

def dfs(x, y):
    if check[x][y] == True:
        return

    check[x][y] = True
    num = [x, y, s - x - y]
    for i in range(3):
        for j in range(3):
            if num[i] < num[j]:
                tmp = [x, y, s - x - y]
                tmp[i] += num[i]
                tmp[j] -= num[i]
                dfs(tmp[0], tmp[1])

check = [[False] * 1501 for _ in range(1501)]
a, b, c = map(int, input().split())
s = a + b + c

if s % 3 != 0:
    print(0)
else:
    dfs(a, b)
    if check[s // 3][s // 3] == True:
        print(1)
    else:
        print(0)