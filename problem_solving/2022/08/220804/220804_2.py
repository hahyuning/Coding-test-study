from collections import defaultdict

def solution(want, number, discount):
    ans = 0

    for i in range(len(discount) - sum(number) + 1):
        buy = defaultdict(int)
        for j in range(i, i + sum(number)):
            buy[discount[j]] += 1

        for k in range(len(want)):
            x = want[k]

            if x not in buy:
                break

            if buy[x] != number[k]:
                break
        else:
            ans += 1

    return ans

solution(
["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])