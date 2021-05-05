from itertools import permutations

def solution(expression):
    op = ["+", "-", "*"]
    operations = permutations(op)

    ans = 0
    for p in operations:
        num = []
        prev = 0
        expression = list(expression)
        for i, x in enumerate(expression):
            if x in op:
                num.append("".join(expression[prev:i]))
                prev = i + 1
                num.append(x)
        num.append("".join(expression[prev:]))

        for pp in p:
            while pp in num:
                i = num.index(pp)
                num = num[:i - 1] + [str(eval(" ".join(num[i - 1: i + 2])))] + num[i + 2:]

        ans = max(ans, abs(int(num[0])))


solution("100-200*300-500+20")
