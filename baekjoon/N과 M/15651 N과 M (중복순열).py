n, m = map(int, input().split()) # n개 중에 중복을 허락하여 m개를 뽑아 일렬로 나열 (순서 있음)
answer_list = [0] * m # 뽑힌 수를 저장할 리스트


def permutation_with_repetition(index):
    # 종료 조건 : 뽑힌 수가 m개가 되면 종료
    if index == m:
        print(" ".join(map(str, answer_list)))
        return

    # 순열에서 중복 조건만 제거
    for i in range(1, n + 1):
        answer_list[index] = i
        permutation_with_repetition(index + 1)

permutation_with_repetition(0)