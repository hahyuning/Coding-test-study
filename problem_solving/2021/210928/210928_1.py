tri_num = [0] * 1001
for i in range(1, 1001):
    tri_num[i] = i * (i + 1) // 2

t = int(input())
for _ in range(t):
    n = int(input())

    ans = 0
    for i in range(1, n + 1):
        if tri_num[i] > n:
            break
        for j in range(1, n + 1):
            if tri_num[j] > n:
                break
            for k in range(1, n + 1):
                if tri_num[k] > n:
                    break
                if tri_num[i] + tri_num[j] + tri_num[k] == n:
                    ans = 1
                    break
            if ans == 1:
                break
        if ans == 1:
            break

    print(ans)
