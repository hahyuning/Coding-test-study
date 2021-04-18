t = int(input())

# 수의 구성이 오름차순을 이루는 것만 센다.
d = [0] * 10001
d[0] = 1

# i로 만들 수 있는 수들 다 구하기
for i in range(1, 4):
    for j in range(1, 10001):
        if j - i >= 0:
            d[j] += d[j - i]

for _ in range(t):
    n = int(input())
    print(d[n])
