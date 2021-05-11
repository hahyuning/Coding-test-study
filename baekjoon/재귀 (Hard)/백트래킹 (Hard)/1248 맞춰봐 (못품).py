def check(index):
    res = 0
    for i in range(index, -1, -1):
        res += ans[i]
        if sign[i][index] == 0:
            if res != 0:
                return False
        elif sign[i][index] > 0:
            if res <= 0:
                return False
        else:
            if res >= 0:
                return False
    return True

def match(index):
    # 종료 조건: n개의 숫자를 다 찾은 경우
    if index == n:
        return True

    # 대각선이 0인 경우
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and match(index + 1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and match(index + 1):
            return True
    return False

# ----------------------------------------------------------------------
n = int(input())
s = input()

sign = [[0] * n for _ in range(n)] # 각 부분합의 부호를 저장할 리스트
ans = [0] * n # 정답을 저장할 리스트

# 문자열을 행렬로 변환
pnt = 0
for i in range(n):
    for j in range(i, n):
        if s[pnt] == "0":
            sign[i][j] = 0
        elif s[pnt] == "+":
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        pnt += 1

match(0)
print(" ".join(map(str, ans)))

