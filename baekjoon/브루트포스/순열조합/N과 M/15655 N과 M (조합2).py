import sys
n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
answer_list = [0] * m

def combination(start, index):
    # 종료 조건 : 선택된 수의 개수가 m개가 되면 종료
    if index == m:
        print(" ".join(map(str, answer_list)))
        return

    for i in range(start, n):
        answer_list[index] = num_list[i]
        # 선택된 수 다음수부터 시작
        combination(i + 1, index + 1)

combination(0, 0)