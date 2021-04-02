n = int(input())
# d[i] : i를 제곱수의 합으로 나타냈을 때, 필요한 항의 최소 개수
# d[i] = max(d[i - j * j] + 1), 1 <= j ** 2 <= i
d = [0] * (n + 1)

for i in range(1, n + 1):
    # 1의 합으로만 나타내는 경우
    d[i] = i
    j = 1
    while j * j <= i:
        if d[i] > d[i - j * j] + 1:
            d[i] = d[i - j * j] + 1
        j += 1

print(d[n])
