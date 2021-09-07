class Node:
    def __init__(self, key):
        self.key = key
        self.data = []
        self.child = dict()


class Trie:
    def __init__(self):
        self.root = Node(None)

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