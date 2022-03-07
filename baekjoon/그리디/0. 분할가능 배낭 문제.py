def fractional_knapsack(capacity, cargo):
    pack = []

    # 단가 계산 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    # 단가 순 그리디 계산
    ans = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            ans += p[1]
        else:
            fraction = capacity / p[2]
            ans += p[1] * fraction
            break
    return ans