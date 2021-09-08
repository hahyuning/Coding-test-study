def count(stones):
    cnt = 0
    max_val = 0

    for st in stones:
        if st == 0:
            cnt += 1
            max_val = max(max_val, cnt)
        else:
            cnt = 0
    return max_val

def solution(stones, k):
    n = len(stones)

    lt = 0
    rt = max(stones)
    while lt <= rt:
        a = stones[:]
        mid = (lt + rt) // 2

        # mid 명 징검다리 건너기
        for i in range(n):
            a[i] = max(0, a[i] - mid)

        # 연속된 0의 개수 세기
        max_val = count(a)
        if max_val >= k:
            rt = mid - 1
        else:
            lt = mid + 1

    return lt