import heapq

def solution(food_times, k):
    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    #시간이 작은 음식부터 빼야 하므로 우선순위 큐를 사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    #먹기 위해 사용한 시간
    s = 0
    #직전에 다 먹은 음식 시간
    prev = 0

    l = len(food_times)
    #sum_value + (현재의 음식 시간 - 이전의 음식 시간) * 현재 음식 개수와 k 비교
    while s + ((q[0][0] - prev) * l) <= k:
        #현재의 음식을 모두 먹는데 걸리는 시간
        now = heapq.heappop(q)[0]
        #현재 음식을 먹는데 걸리는 시간에서 이전 음식을 먹는데 걸리는 시간 빼서 lengtt 곱하기
        s += (now - prev) * l
        l -= 1
        #이전 음식 시간 재설정
        prev = now

    result = sorted(q, key= lambda x: x[1])
    return result[(k - s) % l][1]