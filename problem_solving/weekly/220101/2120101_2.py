from itertools import product

def check(num2, idx):
    global ans

    if idx == m:
        tmp = str(num1 * int(num2))
        if len(tmp) == target and num_check(tmp):
            ans += 1
        return

    for x in num_list:
        tmp = str(num1 * x)
        if len(tmp) == a[m - idx - 1] and num_check(tmp):
            check(num2 + str(x), idx + 1)

def num_check(num):
    for x in num:
        if int(x) not in num_list:
            return False
    return True

k = int(input())
a = list(map(int, input().split()))
n, m = a[0], a[1]
target = a[-1]
a = a[2:-1]

l = int(input())
num_list = list(map(int, input().split()))

ans = 0
all_list = product(num_list, repeat=n)
for p in all_list:
    num1 = int("".join(list(map(str, p[:n]))))
    check("", 0)

print(ans)
