def next_permutation(numbers):
    i = n - 1
    while i > 0 and numbers[i - 1] >= numbers[i]:
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while numbers[j] <= numbers[i - 1]:
        j -= 1

    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]

    j = n - 1
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1

    return True

t = int(input())
for _ in range(t):
    s = list(input())
    n = len(s)
    num = [0] * n
    for i in range(n):
        num[i] = ord(s[i]) - ord("A")

    if next_permutation(num):
        ans = ""
        for x in num:
            ans += chr(x + ord("A"))
        print(ans)
    else:
        print("".join(s))