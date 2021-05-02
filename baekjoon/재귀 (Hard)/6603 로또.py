def rotto(index, result):
    # 종료 조건: 6개의 숫자를 뽑은 경우
    if len(result) == 6:
        print(" ".join(map(str, result)))
        return
    # 종료 조건: 6개의 숫자를 못뽑았지만 범위 초과인 경우
    if index == len(a):
        return

    rotto(index + 1, result + [a[index]])
    rotto(index + 1, result)

# -----------------------------------------
while True:
    n, *a = list(map(int, input().split()))
    if n == 0:
        break

    rotto(0, [])
    print()

