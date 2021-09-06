# 10828 - 스택 
# 기본 스택 자료구조 파일로써 완성하면
# 복사해서 파일하나 빼놓기

class Node():
    def __init__(self, data):
        self.next = None
        self.data = data


class Stack():

    def __init__(self):
        self.top_node = None
        self.first_node = None
        self.element = 0

    def push(self, item):
        new_node = Node(item)
        if self.top_node == None:
            self.top_node = new_node
            self.first_node = new_node
        else:
            self.top_node.next = new_node
            self.top_node = new_node
        self.element += 1

    def pop(self):
        if self.top_node == None:
            return -1
        else:
            temp = self.first_node
            pop_data = self.top_node.data
            for i in range(self.element - 1):
                temp = self.first_node.next
                self.top_node = temp
                self.top_node.next = None
            return pop_data

    def size(self):
        return self.element

    def empty(self):
        if self.element == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.top_node == None:
            return -1
        else:
            return self.top_node.data

