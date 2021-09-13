# 18258 - 큐 2
# 다만들면 큐 자료구조 하나 복사해서 뽑아놓기

# 노드 구상부터 다시 시작!
class Node():
    def __init__(self, data):
        self.next_node = None
        self.data = data

class Queue():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.element = 0

    def push(self, data):
        new_node = Node()
        new_node.data = data
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.next_node = new_node
            self.head = new_node
        self.element += 1

    def pop(self):
        if self.head == None:
            return -1
        else:
            temp = self.tail
            self.tail = temp.next_node
            result = temp.data
            del temp
            self.element -= 1
            return result

    def size(self):
        return self.element

    def empty(self):
        if self.element == 0:
            return 1
        else:
            return 0

    def front(self):
        pass

    def back(self):
        pass