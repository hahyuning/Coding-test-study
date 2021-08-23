n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

answer_list = [0] * m # 선택된 수를 저장할 리스트
check_list = [False] * n # 수를 사용했는지의 여부를 저장할 리스트

def permutation(index):
    # 종료 조건 : 선택된 수가 m개가 되면 종료
    if index == m:
        print(" ".join(map(str, answer_list)))
        return

    for i in range(n):
        # i번째 수가 사용되었는지 확인
        if check_list[i]:
            continue

        check_list[i] = True
        answer_list[index] = num_list[i]
        permutation(index + 1)
        check_list[i] = False

permutation(0)