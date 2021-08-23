n = int(input())
# 각각의 수가 3으로 몇번 나눌 수 있는지 확인
b = list(map(int, input().split()))
a = []

for i in range(n):
    x = b[i]
    cnt = 0
    while x % 3 == 0:
        x //= 3
        cnt += 1
    a.append((cnt, b[i]))
a.sort(key=lambda x:(-x[0], x[1]))

for x, y in a:
    print(y, end=" ")