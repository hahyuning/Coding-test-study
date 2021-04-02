import sys
n, m = map(int, sys.stdin.readline().split()) # n개 중 m개를 뽑는 경우의 수 (순서 없음)
answer_list = [0] * m # 뽑힌 수를 저장할 리스트

def combination(start, index):
    # 종료 조건 : 선택된 수의 개수가 m개가 되면 종료
    if index == m:
        print(" ".join(map(str, answer_list)))
        return

    for i in range(start, n + 1):
        answer_list[index] = i
        # 선택된 수 다음수부터 시작
        combination(i + 1, index + 1)

combination(1, 0)