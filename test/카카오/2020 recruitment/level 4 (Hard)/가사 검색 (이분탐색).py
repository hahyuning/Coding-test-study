from bisect import bisect_left, bisect_right

def count(target, left, right):
    i = bisect_right(target, right)
    j = bisect_left(target, left)
    return i - j

def solution(words, queries):

    list_by_length = [[] for _ in range(10001)]
    # 맨 앞에 ?가 오는 경우를 처리하기 위해 단어를 뒤집어서 저장
    reverse_list = [[] for _ in range(10001)]
    for x in words:
        list_by_length[len(x)].append(x)
        reverse_list[len(x)].append(x[::-1])

    # 리스트 정렬
    for i in range(10001):
        list_by_length[i].sort()
        reverse_list[i].sort()

    ans = []
    for q in queries:
        if q[0] != "?":
            target = list_by_length[len(q)]
        else:
            q = q[::-1]
            target = reverse_list[len(q)]

        res = count(target, q.replace("?", "a"), q.replace("?", "z"))
        ans.append(res)

    return ans