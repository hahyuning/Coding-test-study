n = int(input())
numbers = [i for i in range(1, n + 1)]

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
    print(" ".join(map(str, numbers)))

    if not next_permutation(numbers):
        break