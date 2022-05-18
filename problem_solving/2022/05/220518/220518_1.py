from collections import defaultdict

if __name__ == '__main__':
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    check = defaultdict(bool)
    for x in a:
        check[x] = True

    if check[c]:
        print(1)
    else:
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                # 2개
                if a[i] + a[j] == c:
                    ans = 1
                    break

                # 3개
                if a[i] + a[j] < c:
                    diff = c - (a[i] + a[j])
                    if check[diff] and diff != a[i] and diff != a[j]:
                        ans = 1
                        break
            if ans:
                break

        print(ans)

