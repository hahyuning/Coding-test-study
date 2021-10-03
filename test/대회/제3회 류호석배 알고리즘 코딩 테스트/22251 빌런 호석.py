def dfs(idx, res, cnt):
    global ans

    if idx == k:
        if int(res) not in check:
            check[int(res)] = True
            if cnt <= p and 1 <= int(res) <= n:
                ans += 1
        return

    j = int(str_x[idx])
    for i in range(10):
        tmp = res[:idx] + str(i) + res[idx + 1:]
        dfs(idx + 1, tmp, cnt + diff[i][j])

n, k, p, x = map(int, input().split())

bin_num = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010,
           0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011]
diff = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        xor = bin_num[i] ^ bin_num[j]
        while xor != 0:
            if xor & 1:
                diff[i][j] += 1
            xor >>= 1

check = dict()
str_x = str(x).zfill(k)
ans = 0
dfs(0, str_x, 0)
print(ans - 1)