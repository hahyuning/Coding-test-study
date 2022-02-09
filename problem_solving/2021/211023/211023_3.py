def solution(size):
    ans = []
    for i in range(1, size):
        for j in range(1, size - i):
            k = size - i - j

            max_val = max(i, j, k)
            tmp = [i, j, k]
            s = set(tmp)
            if max_val == i:
                if i < j + k:
                    if s not in ans:
                        ans.append(s)
            elif max_val == j:
                if j < i + k:
                    if s not in ans:
                        ans.append(s)
            else:
                if k < i + j:
                    if s not in ans:
                        ans.append(s)

    return len(ans)

solution(9)