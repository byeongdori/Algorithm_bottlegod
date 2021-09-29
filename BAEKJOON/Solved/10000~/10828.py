# 10828 - 스택 
# 빠른 입출력 사용
# 기본 스택 자료구조 파일로써 완성하면
# 복사해서 파일하나 빼놓기

import sys

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

num = int(input())
stack = Stack()
for i in range (num):
    input_split = list(map(str, sys.stdin.readline().split()))
    if input_split[0] == "push":
        stack.push(int(input_split[1]))
    elif input_split[0] == "pop":
        print(stack.pop())
    elif input_split[0] == "size":
        print(stack.size())
    elif input_split[0] == "empty":
        print(stack.empty())
    elif input_split[0] == "top":
        print(stack.top())