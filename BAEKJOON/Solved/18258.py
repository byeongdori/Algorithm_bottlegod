# 18258 - 큐 2

import sys
from collections import deque

num = int(sys.stdin.readline())
queue = deque()

def push(queue, x):
    queue.append(x) 

def pop(queue): 
    if not queue: 
        return -1 
    else: 
        return queue.popleft() 
    
def size(): 
    return len(queue)

def empty(): 
    if not queue: 
        return 1 
    else: 
        return 0 
    
def front(): 
    if not queue: 
        return -1 
    else: 
        return queue[0] 

def back(): 
    if not queue:
        return -1 
    else: 
        return queue[-1] 

for i in range(num): 
    input_split = sys.stdin.readline().split() 
    if (input_split[0] == "push"): 
        push(queue, input_split[1]) 
    elif(input_split[0] == "pop"): 
        print(pop(queue)) 
    elif(input_split[0] == "size"): 
        print(size()) 
    elif(input_split[0] == "empty"): 
        print(empty()) 
    elif(input_split[0] == "front"): 
        print(front()) 
    elif(input_split[0] == "back"): 
        print(back())