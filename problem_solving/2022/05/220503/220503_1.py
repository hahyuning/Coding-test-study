if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    asc = [1] * n
    desc = [1] * n
    for i in range(1, n):
        if a[i - 1] <= a[i]:
            asc[i] = max(asc[i], asc[i - 1] + 1)
        if a[i - 1] >= a[i]:
            desc[i] = max(desc[i], desc[i - 1] + 1)

    print(max(max(asc), max(desc)))