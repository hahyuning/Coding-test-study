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

def permutation_with_repetition(index):
    print(ans)
    if index == n:
        return True

    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and permutation_with_repetition(index + 1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and permutation_with_repetition(index + 1):
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

permutation_with_repetition(0)
print(" ".join(map(str, ans)))

