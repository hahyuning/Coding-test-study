# Node 클래스
# key: 해당 노드의 문자, child: 자식 노드
# data: 문자열이 끝나는 위치를 알려주는 역할 (해당 노드에서 끝나는 문자열이 없으면 None)
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = dict()


# Trie 클래스
class Trie:
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head

        # 삽입할 string의 각각의 문자에 대해 자식 Node를 만든다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 새로운 Node 생성
            if char not in curr_node.child:
                curr_node.child[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고 해당 노드로 이동
            curr_node = curr_node.child[char]

        # 문자열이 끝난 지점의 노드의 data 값에 해당 문자열 입력
        curr_node.data = string

    # 문자열 조회
    def search(self, string):
        # 가장 위에 있는 노드에서부터 탐색 시작
        curr_node = self.head

        for char in string:
            if char in curr_node.child:
                curr_node = curr_node.child[char]
            else:
                return False

        # 탐색이 끝난 후 해당 노드의 data 값이 존재한다면 탐색 성공
        if curr_node.data != None:
            return True
        return False