import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, self.head, None)
        self.head.next = self.tail
        self.cursor = self.tail

    def insertNode(self, now_node, data):
        prev_node = now_node.prev
        new_node = Node(data, prev_node, now_node)
        now_node.prev = new_node
        prev_node.next = new_node

    def deleteNode(self, now_node):
        prev_node = now_node.prev
        next_node = now_node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def printList(self):
        node = self.head.next
        while node != self.tail:
            print(node.data, end="")
            node = node.next


n = int(input())

for _ in range(n):
    s = input().rstrip()
    linked_list = LinkedList()

    for command in s:
        if command == "<":
            if linked_list.cursor.prev.prev != None:
                linked_list.cursor = linked_list.cursor.prev
        elif command == ">":
            if linked_list.cursor.next != None:
                linked_list.cursor = linked_list.cursor.next
        elif command == "-":
            if linked_list.cursor.prev.prev != None:
                linked_list.deleteNode(linked_list.cursor.prev)
        else:
            linked_list.insertNode(linked_list.cursor, command)

    linked_list.printList()
    print()
