from itertools import combinations
from bisect import bisect_left

class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, words, score):
        curr_node = self.root

        for word in words:
            if word not in curr_node:
                curr_node[word] = dict()
            curr_node = curr_node[word]

        if "score" not in curr_node:
            curr_node["score"] = [score]
        else:
            curr_node["score"].append(score)
            curr_node["score"].sort()

    def search(self, idx, words, score, t):
        if idx == 4:
            return len(t["score"]) - bisect_left(t["score"], score)

        if idx == 0:
            curr_node = t.root
        else:
            curr_node = t

        ans = 0
        if words[idx] == "-":
            for nxt_t in curr_node.values():
                ans += self.search(idx + 1, words, score, nxt_t)
        else:
            if words[idx] in curr_node:
                ans += self.search(idx + 1, words, score, curr_node[words[idx]])

        return ans

def solution(info, query):
    answer = []

    t = Trie()
    for information in info:
        tmp = information.split(" ")
        words = tmp[:-1]
        score = int(tmp[-1])
        t.insert(words, score)

    for q in query:
        tmp = q.replace(" and ", " ").split(" ")
        words = tmp[:-1]
        score = int(tmp[-1])
        cnt = t.search(0, words, score, t)
        answer.append(cnt)

    return answer

#------------------------------------------------------------
def solution2(info, querys):
    answer = []
    dic = {}

    for i in range(len(info)):
        infol = info[i].split()
        key = infol[0:4]
        value = int(infol[4])

        for j in range(5):
            for c in combinations(key, j):
                tmp = ''.join(c)
                if tmp in dic:
                    dic[tmp].append(value)
                else:
                    dic[tmp] = [value]

    for k in dic:
        dic[k].sort()

    for q in querys:
        query = q.split(' ')
        qkey = query[:-1]
        qvalue = int(query[-1])

        while 'and' in qkey:
            qkey.remove('and')
        while '-' in qkey:
            qkey.remove('-')
        qkey = ''.join(qkey)

        if qkey in dic:
            scores = dic[qkey]
            if scores:
                enter = bisect_left(scores, qvalue)
                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer