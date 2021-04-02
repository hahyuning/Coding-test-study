n = int(input())
# d[n] : 2xn 직사각형을 채우는 경우의 수
# d[n] = d[n - 1] + d[n - 2] * 2
d = [0] * 1001
d[0] = 1
d[1] = 1

for i in range(2, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 10007

print(d[n])