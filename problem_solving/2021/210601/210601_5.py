import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input().rstrip()
    k = int(input())

    if k == 1:
        print(1, 1)
    else:
        min_len = len(w) + 1
        max_len = -1
        cnt = [[] for _ in range(26)]
        for i, x in enumerate(w):
            cnt[ord(x) - ord("a")].append(i)

        for x in cnt:
            if len(x) < k:
                continue
            for j in range(len(x) - k + 1):
                min_len = min(min_len, x[j + k - 1] - x[j] + 1)
                max_len = max(max_len, x[j + k - 1] - x[j] + 1)

        if max_len == -1 or min_len == len(w) + 1:
            print(-1)
        else:
            print(min_len, max_len)