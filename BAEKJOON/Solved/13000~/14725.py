# 14725 - 개미굴
# 트라이 자료구조

import sys

class Node():
    def __init__(self, key):
        self.key = key
        self.children = dict()

class Trie():
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, inputstring):
        current_node = self.root
        for i in inputstring:
            if i not in current_node.children:
                current_node.children[i] = Node(i)
            current_node = current_node.children[i]

    def printTrie(self, depth, current_node):
        if depth == 0:
            current_node = self.root
        for i in sorted(current_node.children.keys()):
            print("--" * depth, i, sep="")
            self.printTrie(depth + 1, current_node.children[i])

N = int(input())

t = Trie()
for _ in range(N):
    temp = list(sys.stdin.readline().split())
    t.insert(temp[1:])

t.printTrie(0, None)
