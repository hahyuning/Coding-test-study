def solution(board, moves):
    stack = []
    answer = 0
    for move in moves:
        for i in range(len(board)):
            # 인형이 있는 경우
            if board[i][move - 1] != 0:
                # 스택이 비어있지 않고 똑같은 인형이 두개 모인 경우
                if len(stack) != 0 and stack[-1] == board[i][move - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
    return answer