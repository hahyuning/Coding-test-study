n = int(input())
boj = " " + input()

# d[i]: i번째 문자까지 만들 때 필요한 에너지의 최솟값
d = [-1] * (n + 1)
d[1] = 0

for i in range(1, n + 1):
    if d[i] != -1:
        if boj[i] == "B":
            for j in range(i + 1, n + 1):
                if boj[j] == "O":
                    if d[j] == -1 or d[j] > d[i] + (i - j) ** 2:
                        d[j] = d[i] + (i - j) ** 2
        if boj[i] == "O":
            for j in range(i + 1, n + 1):
                if boj[j] == "J":
                    if d[j] == -1 or d[j] > d[i] + (i - j) ** 2:
                        d[j] = d[i] + (i - j) ** 2
        if boj[i] == "J":
            for j in range(i + 1, n + 1):
                if boj[j] == "B":
                    if d[j] == -1 or d[j] > d[i] + (i - j) ** 2:
                        d[j] = d[i] + (i - j) ** 2

print(d[n])