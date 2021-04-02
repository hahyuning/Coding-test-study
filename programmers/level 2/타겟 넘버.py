def solution(numbers, target):
    n = len(numbers)
    cnt = 0

    def dfs(i, result):
        nonlocal cnt

        if i == n:
            if result == target:
                cnt += 1
            return
        else:
            dfs(i + 1, result + numbers[i])
            dfs(i + 1, result - numbers[i])

    dfs(0, 0)
    return cnt

print(solution([1, 1, 1, 1, 1], 3))