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

while True:
    n, *a = list(map(int,input().split()))
    if n == 0:
        break

    # 0이면 선택 X, 1이면 선택
    d = [0] * (n - 6) + [1] * 6
    ans = []
    while True:
        cur = [a[i] for i in range(n) if d[i] == 1]
        ans.append(cur)
        if not next_permutation(d):
            break

    ans.sort()
    for v in ans:
        print(' '.join(map(str,v)))
    print()