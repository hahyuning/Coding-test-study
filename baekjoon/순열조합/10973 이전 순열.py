n = int(input())
numbers = list(map(int, input().split()))

def prev_permutation(numbers):

    i = n - 1
    while i > 0 and numbers[i - 1] <= numbers[i]:
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while numbers[j] >= numbers[i - 1]:
        j -= 1

    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]

    j = n - 1
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1

    return True

if prev_permutation(numbers):
    print(" ".join(map(str, numbers)))
else:
    print(-1)