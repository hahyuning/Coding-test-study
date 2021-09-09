from itertools import permutations

def solution(expression):
    operation = ["+", "-", "*"]
    priority = permutations(operation)
    num = []
    prev = ""
    for x in expression:
        if x in operation:
            num.append(prev)
            prev = ""
            num.append(x)
        else:
            prev += x
    num.append(prev)

    ans = 0
    for p in priority:
        x = num[:]

        for op in p:
            while op in x:
                idx = x.index(op)
                x = x[:idx - 1] + [str(eval("".join(x[idx - 1:idx + 2])))] + x[idx + 2:]
        ans = max(ans, abs(int(x[0])))

    return ans

solution("100-200*300-500+20")
