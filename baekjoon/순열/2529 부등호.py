def next_permutation(numbers):
    i = n
    while i > 0 and numbers[i - 1] >= numbers[i]:
        i -= 1
    if i <= 0:
        return False

    j = n
    while numbers[j] <= numbers[i - 1]:
        j -= 1
    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]

    j = n
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1
    return True

def prev_permutation(numbers):
    i = n
    while i > 0 and numbers[i - 1] <= numbers[i]:
        i -= 1
    if i <= 0:
        return False

    j = n
    while numbers[j] >= numbers[i - 1]:
        j -= 1
    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]

    j = n
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1
    return True

def check(num):
    for i in range(n):
        if a[i] == "<" and num[i] > num[i + 1]:
                return False
        elif a[i] == ">" and num[i] < num[i + 1]:
                return False
    return True

n = int(input())
a = list(input().split())

smallest = []
largest = []

for i in range(n + 1):
    smallest.append(i)
    largest.append(9 - i)

while True:
    # 부등호를 만족한다면 break
    if check(smallest):
        break
    # 다음 순열이 존재하지 않는다면 break
    if not next_permutation(smallest):
        break

while True:
    if check(largest):
        break
    if not prev_permutation(largest):
        break

print("".join(map(str, largest)))
print("".join(map(str, smallest)))