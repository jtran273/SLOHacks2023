class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        new_Node = Node(newdata)
        new_Node.next = self.head
        self.head = new_Node

    def search(self, perk):
        current = self.head
        while current != None:
            if current.data == perk:
                return True
            current = current.next
        return False
