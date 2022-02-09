change = {0:[1, 1, 0, 1, 0, 0, 0, 0, 0],
          1:[1, 1, 1, 0, 1, 0, 0, 0, 0],
          2:[0, 1, 1, 0, 0, 1, 0, 0, 0],
          3:[1, 0, 0, 1, 1, 0, 1, 0, 0],
          4:[0, 1, 0, 1, 1, 1, 0, 1, 0],
          5:[0, 0, 1, 0, 1, 1, 0, 0, 1],
          6:[0, 0, 0, 1, 0, 0, 1, 1, 0],
          7:[0, 0, 0, 0, 1, 0, 1, 1, 1],
          8:[0, 0, 0, 0, 0, 1, 0, 1, 1]}

n = int(input())
for _ in range(n):
    target = []
    ans = 2 ** 9
    for _ in range(3):
        tmp = input()
        for x in tmp:
            if x == "*":
                target.append(1)
            else:
                target.append(0)

    for i in range(1 << 9):
        a = [0] * 9
        cnt = 0
        for j in range(9):
            if i & (1 << j):
                cnt += 1
                for k in range(9):
                    a[k] = a[k] ^ change[j][k]

        if a == target:
            ans = min(ans, cnt)
    print(ans)
