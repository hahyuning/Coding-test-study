import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
num_list = list(map(int, input().split()))

cnt = 0
for x in num_list:
    if x == 1:
        continue
    if is_prime_number(x):
        cnt += 1

print(cnt)