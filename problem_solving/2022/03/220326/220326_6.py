import heapq
from collections import defaultdict

def solution(req_id, req_info):
    gold = defaultdict(int)
    silver = defaultdict(int)
    sell = []
    buy = []
    for i in range(len(req_id)):
        # 구매
        if req_info[i][0] == 0:
            buy_amount = req_info[i][1]
            buy_price = req_info[i][2]

            if not sell:
                heapq.heappush(buy, (-buy_price, i, buy_amount, req_id[i]))
                continue

            while sell and buy_amount > 0:
                sell_price, num, sell_amount, name = heapq.heappop(sell)
                if sell_price > buy_price:
                    heapq.heappush(sell, (sell_price, i,  sell_amount, name))
                    break

                if buy_amount <= sell_amount:
                    gold[req_id[i]] += buy_amount
                    gold[name] -= buy_amount
                    silver[req_id[i]] -= buy_amount * sell_price
                    silver[name] += buy_amount * sell_price
                    sell_amount -= buy_amount
                    buy_amount = 0

                    if sell_amount > 0:
                        heapq.heappush(sell, (sell_price, i, sell_amount, name))
                else:
                    gold[req_id[i]] += sell_amount
                    gold[name] -= sell_amount
                    silver[req_id[i]] -= sell_amount * sell_price
                    silver[name] += sell_amount * sell_price
                    buy_amount -= sell_amount

            if buy_amount > 0:
                heapq.heappush(buy, (-buy_price, i, buy_amount, req_id[i]))

        else:
            sell_amount = req_info[i][1]
            sell_price = req_info[i][2]

            if not buy:
                heapq.heappush(sell, (sell_price, i, sell_amount, req_id[i]))
                continue

            while buy and sell_amount > 0:
                buy_price, num, buy_amount, name = heapq.heappop(buy)
                buy_price = -buy_price

                if buy_price < sell_price:
                    heapq.heappush(buy, (-buy_price, i, buy_amount, name))
                    break

                if buy_amount >= sell_amount:
                    gold[name] += sell_amount
                    gold[req_id[i]] -= sell_amount
                    silver[name] -= sell_amount * sell_price
                    silver[req_id[i]] += sell_amount * sell_price
                    buy_amount -= sell_amount
                    sell_amount = 0

                    if buy_price > 0:
                        heapq.heappush(buy, (-buy_price, i, buy_amount, name))
                else:
                    gold[name] += buy_amount
                    gold[req_id[i]] -= buy_amount
                    silver[name] -= buy_amount * sell_price
                    silver[req_id[i]] += buy_amount * sell_price
                    sell_amount -= buy_amount

            if sell_amount > 0:
                heapq.heappush(sell, (sell_price, i, sell_amount, req_id[i]))

        print("buy")
        print(buy)
        print("sell")
        print(sell)
        print(gold)
        print(silver)
    req_id.sort()
    ans = []
    for x in req_id:
        tmp = x
        if gold[x] > 0:
            tmp += " +" + str(gold[x])
        elif gold[x] == 0:
            tmp += " 0"
        else:
            tmp += " " + str(gold[x])

        if silver[x] > 0:
            tmp += " +" + str(silver[x])
        elif silver[x] == 0:
            tmp += " 0"
        else:
            tmp += " " + str(silver[x])

        if tmp not in ans:
            ans.append(tmp)

    print(ans)
    return ans

solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"], [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]])