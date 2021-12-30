prime = [False] * 1001
prime[1] = True

for i in range(2, 1001):
    if prime[i] == False:
        for j in range(2 * i, 1001, i):
            prime[j] = True

n = int(input())
num = list(map(int, input().split()))
cnt = 0
for x in num:
    if prime[x] == False:
        cnt += 1
print(cnt)