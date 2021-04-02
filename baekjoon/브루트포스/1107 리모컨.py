n = int(input())
m = int(input())
broken = [False] * 10

if m > 0:
    a = list(map(int, input().split()))
else:
    a = []

for x in a:
    broken[x] = True

def possible(ch):
    if ch == 0:
        # 0번이 고장났다면
        if broken[0]:
            return 0
        else:
            return 1

    l = 0
    while ch > 0:
        if broken[ch % 10]:
            return 0
        l += 1
        ch //= 10
    # 누른 횟수 반환
    return l

# 100번에서 숫자 버튼을 누르지 않고 이동하는 횟수로 지정
ans = abs(n - 100)

for i in range(1000001):
    cnt = possible(i)
    if cnt > 0:
        ans = min(ans, abs(i - n) + cnt)

print(ans)