n = int(input())
a = [int(input()) for _ in range(n)]

last = 0
cnt = 0
for x in a:
    if x > last:
        cnt += 1
        last = x
print(cnt)

last = 0
cnt = 0
for x in a[::-1]:
    if x > last:
        cnt += 1
        last = x
print(cnt)