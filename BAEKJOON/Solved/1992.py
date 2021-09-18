# 1992 - 쿼드 트리

import sys

size = int(input())

arr = []

for i in range(0, size):
    arr.append(list(map(int, input())))

def quad_tree(array, x, y, size):
    
    color = array[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if array[i][j] != color:
                sys.stdout.write("(")
                quad_tree(array, x, y, size //2)
                quad_tree(array, x, y + size // 2, size // 2)
                quad_tree(array, x + size // 2, y, size // 2)
                quad_tree(array, x + size // 2, y + size // 2, size // 2)
                sys.stdout.write(")")
                return

    sys.stdout.write(str(color))

quad_tree(arr, 0, 0, size)