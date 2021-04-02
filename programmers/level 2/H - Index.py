def solution(citations):
    citations.sort(reverse=True)

    for i, n in enumerate(citations):
        if n <= i:
            return i
    return len(citations)

solution([3, 0, 6, 1, 5])