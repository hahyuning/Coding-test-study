from itertools import combinations

if __name__ == '__main__':

    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    C = combinations([i for i in range(m)], 3)

    max_sum = 0
    for c in C:
        tmp_sum = 0
        for i in range(n):
            tmp = 0
            for j in c:
                tmp = max(tmp, a[i][j])
            tmp_sum += tmp
        max_sum = max(tmp_sum, max_sum)

    print(max_sum)