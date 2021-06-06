def division2(a, b):
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            print(i)

def division3(a, b, c):
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            print(i)

n = int(input())
num = list(map(int, input().split()))
if n == 2:
    division2(num[0], num[1])
else:
    division3(num[0], num[1], num[2])