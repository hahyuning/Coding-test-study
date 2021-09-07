def solution(n, arr1, arr2):
    ans = []

    for x, y in zip(arr1, arr2):
        # or 연산
        res = bin(x|y)[2:]

        tmp = ""
        if len(res) != n:
            tmp += " " * (n - len(res))
        for x in res:
            if x == "1":
                tmp += "#"
            else:
                tmp += " "
        ans.append(tmp)
    return ans
