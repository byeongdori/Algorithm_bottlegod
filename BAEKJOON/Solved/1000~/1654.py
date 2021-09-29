# 1654 - 랜선 자르기
# 이분 탐색

input_split = input().split()
n = int(input_split[0])
k = int(input_split[1])

lan_len = []
for i in range(n):
    lan_len.append(int(input()))

short, long = 1, max(lan_len)

while short <= long:
    mid = (short + long) // 2
    lan_count = 0
    for i in lan_len:
        lan_count += i // mid
    if lan_count >= k:
        short = mid + 1
    else:
        long = mid - 1

print(long)