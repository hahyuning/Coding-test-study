n = int(input())
numbers = [i for i in range(1, n + 1)]

def next_permutation(numbers):
    # 감수하는 수열의 가장 큰 시작점 바로 이전 인덱스 찾기 (while 문 반복 이후 -1)
    i = n - 1
    while i > 0 and numbers[i - 1] >= numbers[i]:
        i -= 1
    # 수열 전체가 감소하는 경우 다음 순열 X
    if i <= 0:
        return False

    # 위에서 찾은 자리의 숫자보다 큰 숫자 중 가장 큰 인덱스 찾기
    j = n - 1
    while numbers[j] <= numbers[i - 1]:
        j -= 1

    # 두 수 자리 교체
    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]

    # i 번째 이후의 숫자 뒤집기
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