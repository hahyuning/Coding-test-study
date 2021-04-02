import math
n = int(input())
array = [True for i in range(n + 1)]
array[1] = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

answer = 0
for i in range(1, n + 1):
    if array[i]:
        answer += 1