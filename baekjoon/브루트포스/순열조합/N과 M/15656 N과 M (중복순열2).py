n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
answer_list = [0] * m

def permutation_with_repetition(index):
    # 종료 조건 : 뽑힌 수가 m개가 되면 종료
    if index == m:
        print(" ".join(map(str, answer_list)))
        return

    # 순열에서 중복 조건만 제거
    for i in range(n):
        answer_list[index] = num_list[i]
        permutation_with_repetition(index + 1)

permutation_with_repetition(0)