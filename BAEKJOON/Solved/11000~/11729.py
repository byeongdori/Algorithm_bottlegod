# 11729 - 하노이 탑 이동 순서
# 재귀함수를 이용한 문제 해석

def move_hanoi(num_of_pan, start, to, via):
    if num_of_pan == 1:
        print(start, to)
    else:
        move_hanoi(num_of_pan - 1, start, via, to) # 1번의 n - 1개를 2번으로 이동
        print(start, to) # 1번 남은 1개를 3번으로 이동
        move_hanoi(num_of_pan - 1, via, to, start) # 2번의 n - 1개를 3번으로 이동


total_pan = int(input())
total_move = pow(2, total_pan) - 1
print(total_move)
move_hanoi(total_pan, 1, 3, 2)