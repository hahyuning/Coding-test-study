class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = []
        self.child = dict()

# Trie 클래스
class Trie:
    def __init__(self):
        self.root = Node(None)

    # 문자열 삽입
    def insert(self, word):
        curr_node = self.root

        for char in word:
            if char not in curr_node.child:
                curr_node.child[char] = Node(char)

            curr_node.data.append(word)
            curr_node = curr_node.child[char]

        curr_node.data.append(word)


    def search(self, word):
        curr_node = self.root

        cnt = 0
        for char in word:
            if len(curr_node.data) == 1:
                break

            cnt += 1
            curr_node = curr_node.child[char]

        return cnt

def solution(words):
    ans = 0
    trie = Trie()

    for x in words:
        trie.insert(x)

    for x in words:
        ans += trie.search(x)

    return ans

solution(["word","war","warrior","world"])