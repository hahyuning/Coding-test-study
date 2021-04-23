num = [int(input()) for _ in range(9)]
num.sort()
s = sum(num)

ans = []
for i, x in enumerate(num):
    for j, y in enumerate(num):
        if i == j:
            continue
        if s - x - y == 100:
            ans = num[:i] + num[i + 1:j] + num[j + 1:]
            for n in ans:
                print(n)
            exit(0)

