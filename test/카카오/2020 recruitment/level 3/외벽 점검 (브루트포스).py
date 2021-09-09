from itertools import permutations

def solution(n, weak, dist):
    m = len(weak)
    # weak 일자로 늘리기
    weak += [x + n for x in weak]

    ans = -1
    # weak 의 각 위치를 시작점으로
    for s in range(m):
        # 가능한 모든 친구 순서 확인
        for order in list(permutations(dist)):
            cnt = 0 # 현재 투입된 친구의 수
            now = weak[s] + order[cnt] # 현재까지 검사를 완료한 지점

            for i, x in enumerate(weak[s:s + m], start=s):
                # 현재 인원만으로 검사를 할 수 없는 경우
                if now < x:
                    if cnt + 1 >= len(dist):
                        break

                    # 새로운 인원 추가가
                    cnt += 1
                    now = weak[i] + order[cnt]
            else:
                if ans == -1 or cnt + 1 < ans:
                    ans = cnt + 1
    return ans
