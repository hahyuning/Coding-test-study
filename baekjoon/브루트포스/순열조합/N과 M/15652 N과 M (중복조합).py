import sys
n, m = map(int, sys.stdin.readline().split()) # n개 중에 중복을 허락하여 m개를 뽑는 경우의 수 (순서 없음)
answer_list = [0] * m # 뽑힌 수를 저장할 리스트


def combination_with_repetition(start, index):
    # 종료 조건 : 뽑힌 수의 개수가 m개가 되면 종료
    if index == m:
        print(" ".join(map(str, answer_list)))
        return

    for i in range(start, n + 1):
        answer_list[index] = i
        combination_with_repetition(i, index + 1)

combination_with_repetition(1, 0)