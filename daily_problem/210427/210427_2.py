n = int(input())
m = n // 5

s = input()
signal = [[0] * m for _ in range(5)]
for i in range(5):
    for j in range(m):
        signal[i][j] = s[m * i + j]

dict = ["####.##.##.####", "", "###..#####..###", "###..####..####", "#.##.####..#..#", "####..###..####",
        "####..####.####", "###..#..#..#..#", "####.#####.####", "####.####..####"]

ans = ""
j = 0
while j < m:
    if signal[0][j] == "#":
        # 범위 검사
        if j + 3 > m:
            ans += "1"
            j += 1
        else:
            tmp = ""
            for i in range(5):
                for k in range(3):
                    tmp += signal[i][j + k]

            if tmp in dict:
                ans += str(dict.index(tmp))
                j += 3
            else:
                ans += "1"
                j += 1
    else:
        j += 1

print(ans)
