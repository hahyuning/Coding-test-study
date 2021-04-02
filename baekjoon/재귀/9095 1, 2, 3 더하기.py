n = int(input())

def permutation_with_repetition(sum, target):
    global cnt
    if sum == target:
        cnt += 1
        return
    if sum > target:
        return

    for i in range(1, 4):
        permutation_with_repetition(sum + i, target)

for _ in range(n):
    target = int(input())
    cnt = 0
    permutation_with_repetition(0, target)
    print(cnt)

