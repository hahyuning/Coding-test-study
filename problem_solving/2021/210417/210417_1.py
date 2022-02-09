n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

min_ans = 10 ** 8
max_ans = -(10 ** 8)

def cal(i, num, plus, minus, mul, div):
    global min_ans, max_ans

    if i == n:
        min_ans = min(min_ans, num)
        max_ans = max(max_ans, num)
        return

    if plus > 0:
        cal(i + 1, num + a[i], plus - 1, minus, mul, div)
    if minus > 0:
        cal(i + 1, num - a[i], plus, minus - 1, mul, div)
    if mul > 0:
        cal(i + 1, num * a[i], plus, minus, mul - 1, div)
    if div > 0:
        if num < 0:
            cal(i + 1, -((-num) // a[i]), plus, minus, mul, div - 1)
        else:
            cal(i + 1, num // a[i], plus, minus, mul, div - 1)

cal(1, a[0], plus, minus, mul, div)
print(max_ans)
print(min_ans)