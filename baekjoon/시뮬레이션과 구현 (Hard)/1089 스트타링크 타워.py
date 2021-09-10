nums = ["###...#.###.###.#.#.###.###.###.###.###",
        "#.#...#...#...#.#.#.#...#.....#.#.#.#.#",
        "#.#...#.###.###.###.###.###...#.###.###",
        "#.#...#.#.....#...#...#.#.#...#.#.#...#",
        "###...#.###.###...#.###.###...#.###.###"]

# x번째 숫자가 y인 것이 가능한지 확인
def check(x, y):
    for i in range(5):
        for j in range(3):
            if nums[i][4 * y + j] == "." and a[i][4 * x + j] == "#":
                return False
    return True

n = int(input())
a = [input() for _ in range(5)]
# n번째 자리에 올수 있는 숫자 저장
possible = [[] for _ in range(n)]

for i in range(n):
    for j in range(10):
        if check(i, j):
            possible[i].append(j)

all = 1
for i in range(n):
    all *= len(possible[i])

if all == 0:
    print(-1)
else:
    s = 0
    for i in range(n):
        tmp = 0
        for x in possible[i]:
            tmp += x

        s = s * 10 + tmp * (all // len(possible[i]))

    print("%.10f" % (s / all))