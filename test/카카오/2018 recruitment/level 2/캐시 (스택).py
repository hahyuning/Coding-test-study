def solution(cacheSize, cities):
    # LRU: 메모리 상에서 가장 최근에 사용된 적이 없는 캐시의 메모리부터 교체
    # 캐시히트: 1, 캐시미스: 5

    ans = 0
    cache = []
    cities = [x.lower() for x in cities]

    if cacheSize == 0:
        return len(cities) * 5

    for x in cities:
        # 캐시 히트인 경우
        if x in cache:
            ans += 1
            idx = cache.index(x)
            cache.pop(idx)
            cache.append(x)
        # 캐시 미스인 경우
        else:
            ans += 5
            if len(cache) < cacheSize:
                cache.append(x)
            else:
                cache.pop(0)
                cache.append(x)

    return ans