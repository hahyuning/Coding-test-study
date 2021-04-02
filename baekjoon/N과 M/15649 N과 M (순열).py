n, m = map(int, input().split()) # n개 중에 m개를 뽑아 일렬로 나열 (순서 있음)
answer_list = [0] * m # 선택된 수를 저장할 리스트
check_list = [False] * (n + 1) # 수를 사용했는지의 여부를 저장할 리스트

def permutation(index):
    # 종료 조건 : 선택된 수가 m개가 되면 종료
    if index == m:
        print(" ".join(map(str, answer_list)))
        return

    for i in range(1, n + 1):
        # 수가 사용되었는지 확인
        if check_list[i]:
            continue

        check_list[i] = True
        answer_list[index] = i
        permutation(index + 1)
        check_list[i] = False

permutation(0)