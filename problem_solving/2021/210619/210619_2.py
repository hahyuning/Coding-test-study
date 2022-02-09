n = int(input())
m = int(input())
rec = list(map(int, input().split()))

# 1. 추천받은 학생의 사진은 반드시 게시
# 2. 게시된 사진이 n개인 경우 현재까지 추천받은 횟수가 가장 적은 학생 -> 게시된지 가장 오래된 학생 우선순위로 삭제
# 3. 사진이 게시된 학생이 추천받는 경우 추천 횟수만 증가
# 4. 게시된 사진이 삭제되는 경우 추천받은 횟수는 0으로 바뀜
pictures = dict()
for i in rec:
    if i not in pictures:
        if len(pictures.keys()) < n:
            pictures[i] = 1
        else:
            tmp = sorted(pictures.items(), key=lambda x:(x[1]))
            num, cnt = tmp[0][0], tmp[0][1]
            del pictures[num]
            pictures[i] = 1
    else:
        pictures[i] += 1

ans = list(pictures.keys())
ans.sort()
print(*ans)