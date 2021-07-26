class Trie:
    def __init__(self):
        self.root = dict()

    # 문자열 삽입
    def insert(self, words):
        curr_node = self.root

        for word in words:
            if word not in curr_node:
                curr_node[word] = dict()
            curr_node = curr_node[word]

        curr_node[0] = True

    def search_all(self, level, node):
        if 0 in node:
            return

        curr_child = sorted(node)
        for ch in curr_child:
            print("--" * level + ch)
            self.search_all(level + 1, node[ch])

n = int(input())
t = Trie()
for _ in range(n):
    x = input().split()
    m = int(x[0])
    t.insert(x[1:])

t.search_all(0, t.root)