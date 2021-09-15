# 18258 - 큐 2

import sys

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
        new_node = Node(data)
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.next_node = new_node
            self.head = new_node
        self.element += 1

    def pop(self):
        if self.tail == None:
            return -1
        else:
            result = self.tail.data
            self.tail = self.tail.next_node
            if self.element == 1:
                self.head = None
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
        if self.head == None:
            return -1
        else:
            return self.head.data

    def back(self):
        if self.tail == None:
            return -1
        else:
            return self.tail.data

num = int(input())
queue = Queue()
for i in range (num):
    input_split = list(map(str, sys.stdin.readline().split()))
    if input_split[0] == "push":
        queue.push(int(input_split[1]))
    elif input_split[0] == "pop":
        sys.stdout.write(str(queue.pop())+"\n")
    elif input_split[0] == "size":
        sys.stdout.write(str(queue.size())+"\n")
    elif input_split[0] == "empty":
        sys.stdout.write(str(queue.empty())+"\n")
    elif input_split[0] == "front":
        sys.stdout.write(str(queue.front())+"\n")
    elif input_split[0] == "back":
        sys.stdout.write(str(queue.back())+"\n")