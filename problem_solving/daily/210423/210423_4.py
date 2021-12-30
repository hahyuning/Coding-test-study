n = int(input())

# d[i]: 버튼을 i번 눌렀을 때 출력할 수 있는 A의 최대 개수
# d[i] = max(d[i - 1] + 1, (j + 1) * d[i - (j + 2)]), 1 <= j <= i - 2
d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = d[i - 1] + 1
    for j in range(1, i - 2):
        d[i] = max(d[i], (j + 1) * d[i - (j + 2)])

print(d[n])