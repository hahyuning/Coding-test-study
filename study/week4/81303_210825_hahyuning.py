import sys
input = sys.stdin.readline

class Node:
    def __init__(self, prev = None, next = None):
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(self.head, None)
        self.head.next = self.tail
        self.cursor = self.tail

    def insertNode(self, now_node):
        prev_node = now_node.prev
        new_node = Node(prev_node, now_node)
        now_node.prev = new_node
        prev_node.next = new_node

    def deleteNode(self, now_node):
        prev_node = now_node.prev
        next_node = now_node.next
        prev_node.next = next_node
        next_node.prev = prev_node

def solution(n, k, cmd):
    ans = []

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])