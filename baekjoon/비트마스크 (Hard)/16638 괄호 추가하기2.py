import sys
# 연산자가 하나만 들어있고, 중첩된 괄호 X
# 무엇을 먼저 계산할지 결정하되, 연속적이어서는 안됨

n = int(input())
a = list(input())

# 연산자의 개수
m = (n - 1) // 2
# 비트마스크 사용
ans = -sys.maxsize
for s in range(1 << m):
    check = False
    # 연속적으로 선택됐는지 확인
    for i in range(m - 1):
        if (s & (1 << i)) > 0 and (s & (1 << (i + 1))) > 0:
            check = True

    if check:
        continue

    # 배열 복사해서 사용
    b = a[:]
    for i in range(m):
        if (s & (1 << i)) > 0:
            # 연산자의 실제 위치
            k = 2 * i + 1
            b[k - 1] = "(" + b[k - 1]
            b[k + 1] = b[k + 1] + ")"

    c = "".join(b)
    tmp = eval(c)
    ans = max(ans, tmp)

print(ans)
