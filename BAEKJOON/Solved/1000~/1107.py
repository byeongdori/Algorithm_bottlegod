# 1107 - 리모컨

N = int(input())
M = int(input())

remote_control = {str(i) for i in range(10)}
if M > 0:
    remote_control -= set(map(str, input().split()))

min_move = abs(100 - N)

for channel in range(1000000):
    for j in range(len(str(channel))):
        if str(channel)[j] not in remote_control:
            break
        elif j == len(str(channel)) - 1:
            min_move = min(min_move, abs(channel - N) + len(str(channel)))

print(min_move)