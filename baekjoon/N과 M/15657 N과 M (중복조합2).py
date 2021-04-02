import sys
n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
answer_list = [0] * m

def combination_with_repetition(start, index):
    # 종료 조건 : 뽑힌 수의 개수가 m개가 되면 종료
    if index == m:
        print(" ".join(map(str, answer_list)))
        return

    for i in range(start, n):
        answer_list[index] = num_list[i]
        combination_with_repetition(i, index + 1)

combination_with_repetition(0, 0)