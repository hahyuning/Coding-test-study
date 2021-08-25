def next_permutation():
    i = 8
    while i > 0 and num[i - 1] >= num[i]:
        i -= 1
    if i <= 0:
        return False

    j = 8
    while num[j] <= num[i - 1]:
        j -= 1
    num[i - 1], num[j] = num[j], num[i - 1]

    j = 8
    while i < j:
        num[i], num[j] = num[j], num[i]
        i += 1
        j -= 1
    return True

def check():
    s = num[0] + num[1] + num[2]

    # 행 검사
    for i in range(3):
        if s != num[i * 3] + num[i * 3 + 1] + num[i * 3 + 2]:
            return False
    # 열 검사
    for j in range(3):
        tmp = 0
        for i in range(3):
            tmp += num[i * 3 + j]

        if s != tmp:
            return False

    # 대각선 검사
    if s != num[0] + num[4] + num[8]:
        return False
    if s != num[2] + num[4] + num[6]:
        return False
    return True

def calculate():
    ans = 0
    for i in range(3):
        for j in range(3):
            ans += abs(a[i][j] - num[i * 3 + j])
    return ans

a = [list(map(int, input().split())) for _ in range(3)]
num = [i for i in range(1, 10)]
ans = 100
while True:
    if check():
        ans = min(ans, calculate())

    if not next_permutation():
        break
print(ans)
