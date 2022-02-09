import bisect
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
dic = dict()
key = []

for _ in range(n):
    a, b = map(int, input().split())
    dic[a] = b
    key.append(a)

key.sort()

for _ in range(m):
    op, *num = map(int, input().split())
    # 데이터 추가
    if op == 1:
        a, b = num[0], num[1]
        dic[a] = b
        bisect.insort(key, a)
    # 데이터 변경
    elif op == 2:
        a, b = num[0], num[1]
        # 키가 존재하는 경우
        if a in key:
            dic[a] = b
            continue

        idx = bisect.bisect_left(key, a)
        if idx == len(key):
            if key[-1] - a <= k:
                dic[key[-1]] = b
        elif idx == 0:
            if a - key[0] <= k:
                dic[key[0]] = b
        else:
            d1 = a - key[idx - 1]
            d2 = key[idx] - a
            if d1 > k and d2 > k:
                continue
            if d1 == d2:
                continue

            if d1 < d2:
                dic[key[idx - 1]] = b
            elif d1 > d2:
                dic[key[idx]] = b
    else:
        num = num[0]
        if num in key:
            print(dic[num])
            continue

        idx = bisect.bisect_left(key, num)
        if idx == len(key):
            if num - key[-1] <= k:
                print(dic[key[-1]])
            else:
                print(-1)
        elif idx == 0:
            if key[0] - num <= k:
                print(dic[key[0]])
            else:
                print(-1)
        else:
            d1 = num - key[idx - 1]
            d2 = key[idx] - num
            if d1 > k and d2 > k:
                print(-1)
                continue
            if d1 == d2:
                print("?")
                continue

            if d1 < d2:
                print(dic[key[idx - 1]])
            elif d1 > d2:
                print(dic[key[idx]])