import sys
sys.setrecursionlimit(1500 * 1500)

def dfs(x, y):
    # (x, y)의 무게를 만들 수 있으면 return
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

# --------------------------------------------------
a, b, c = map(int, input().split())
# 합은 일정하기 때문에 두 개의 변수만으로 처리 가능
s = a + b + c
check = [[False] * 1501 for _ in range(1501)]

# 합이 3으로 안나눠지면 불가능한 경우
if s % 3 != 0:
    print(0)
else:
    dfs(a, b)
    if check[s // 3][s // 3] == True:
        print(1)
    else:
        print(0)