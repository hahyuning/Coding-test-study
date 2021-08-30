n = int(input())
max_len = 0
path = []
for i in range(n + 1):
    a = n
    b = i
    tmp = [a, b]
    while a - b >= 0:
        tmp.append(a - b)
        a, b = b, a - b

    if len(tmp) > max_len:
        max_len = len(tmp)
        path = tmp

print(max_len)
print(*path)