import copy

def solution(stones, k):
    n = len(stones)
    answer = 0
    lt = 0
    rt = max(stones)
    while lt <= rt:
        new_stones = copy.deepcopy(stones)
        mid = (lt + rt) // 2
        for i in range(n):
            new_stones[i] = max(0, new_stones[i] - mid)

        max_val = count(new_stones)
        # 연속된 0의 개수가 k보다 크거나 같은 경우
        if max_val >= k:
            rt = mid - 1
        else:
            answer = mid
            lt = mid + 1

    return answer + 1

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
