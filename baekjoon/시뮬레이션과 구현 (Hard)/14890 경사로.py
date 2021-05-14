def slide(a):
    # 경사로를 놓았는지 확인하기 위한 배열
    c = [False] * n
    for i in range(1, n):
        # 높이가 다른 경우
        if a[i - 1] != a[i]:
            diff = abs(a[i] - a[i - 1])
            # 두 칸의 높이의 차이가 1이 아니면 false
            if diff != 1:
                return False
            # 다음 칸이 더 높은 경우
            if a[i - 1] < a[i]:
                for j in range(1, l + 1):
                    # 범위를 벗어나면 false
                    if i - j < 0:
                        return False
                    # 칸의 높이가 달라지면 false
                    if a[i - 1] != a[i - j]:
                        return False
                    # 이미 경사로가 놓여있으면 false
                    if c[i - j]:
                        return False
                    c[i - j] = True
            # 다음 칸이 더 낮은 경우
            else:
                for j in range(l):
                    if i + j >= n:
                        return False
                    if a[i] != a[i + j]:
                        return False
                    if c[i + j]:
                        return False
                    c[i + j] = True
    return True

# l: 경사로의 길이
n, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# 지나갈 수 있는 길의 개수
ans = 0

# 행에 대해 계산
for i in range(n):
    d = a[i]
    if slide(d):
        ans += 1

# 열에 대해 계산
for j in range(n):
    d = [a[i][j] for i in range(n)]
    if slide(d):
        ans += 1

print(ans)
