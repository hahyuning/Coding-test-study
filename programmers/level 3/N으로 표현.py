def solution(N, number):
    # d[i]: N을 i번 사용해서 만들 수 있는 수
    d = [set() for _ in range(9)]
    for i in range(1, 9):
        d[i].add(int(str(N) * i))

    for i in range(1, 9):
        for j in range(i):
            for x in d[j]:
                for y in d[i - j]:
                    d[i].add(x + y)
                    d[i].add(x - y)
                    d[i].add(x * y)
                    if y != 0:
                        d[i].add(x // y)
        if number in d[i]:
            return i
    return -1
