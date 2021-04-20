n = int(input())

s = 0
while True:
    if s * (s + 1) // 2 > n:
        break
    s += 1

print(s - 1)