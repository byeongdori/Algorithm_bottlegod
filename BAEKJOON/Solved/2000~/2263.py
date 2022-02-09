# 2263 - 트리의 순회
# 재귀 - 매개변수에 들어가는 조건 잘 파악하기!

import sys
sys.setrecursionlimit(10**6)

def preorder(in_start, in_end, post_start, post_end):
    
    if (in_start > in_end) or (post_start > post_end):
        return

    divide = postorder[post_end]
    print(divide, end=' ')

    # divide 기준 남은 좌측 길이
    left = index[divide] - in_start
    # divide 기준 남은 우측 길이
    right = in_end - index[divide]

    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index = [0 for _ in range(100001)]
for i in range(n):
    # inorder[i]의 위치는 inorder 상의 i 번째에 있다!
    index[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)

