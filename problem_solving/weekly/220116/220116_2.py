n = int(input())
len = 0
while 2 ** len - 2 < n:
    len += 1
len -= 1

num = n - 2 ** len + 1
ans = [0] * len
for i in range(len - 1, -1, -1):
    ans[i] = num % 2
    num //= 2

res = ""
for i in range(len):
    if ans[i] == 1:
        res += "7"
    else:
        res += "4"
print(res)