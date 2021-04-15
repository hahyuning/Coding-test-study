n = int(input())
a = list(map(int, input().split()))

check = [False] * 2000000

# 1부터 2의 n승 까지
for i in range(1 << n):
    s = 0
    for j in range(n):
        # j번째 원소의 비트가 1인지 확인
        if i & (1 << j):
            s += a[j]
    check[s] = True

i = 1
while True:
    if not check[i]:
        break
    i += 1
print(i)