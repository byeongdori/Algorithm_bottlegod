# Node를 활용한 Stack 자료구조

class Node():
    def __init__(self, data):
        self.next_node = None
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
            self.top_node.next_node = new_node
            self.top_node = new_node
        self.element += 1

    def pop(self):
        if self.top_node == None:
            return -1
        else:
            pop_data = self.top_node.data
            temp = self.first_node
            if self.element == 1:
                self.top_node = None
                self.first_node = None
                self.element = 0
                return pop_data
            while temp.next_node != self.top_node:
                temp = temp.next_node
            self.top_node = temp
            temp.next_node = None
        self.element -= 1
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
