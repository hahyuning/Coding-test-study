from itertools import permutations

# 스트라이크: 자리 동일
# 볼: 다른 위치

n = int(input())
res = []
for _ in range(n):
    a, b, c = map(int, input().split())
    res.append((str(a), b, c))

ans = 0
c = list(permutations([i for i in range(1, 10)], 3))
for x in c:
    x = "".join(map(str, x))

    for y, c1, c2 in res:
        check = [False] * 3
        strike = 0
        for i in range(3):
            if x[i] == y[i]:
                strike += 1
                check[i] = True

        ball = 0
        for i in range(3):
            if not check[i]:
                if x[i] in y:
                    ball += 1

        if strike != c1 or ball != c2:
            break
    else:
        ans += 1
print(ans)

