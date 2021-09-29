# 1259 - 팰린드롬수

n = int(input())
while (n != 0):
    check = True
    input_list = list(map(int,str(n)))
    for i in range(len(input_list) // 2):
        if input_list[i] != input_list[len(input_list) -1 - i]:
            check = False
            break
    if check:
        print("yes")
    else:
        print("no")
    n = int(input())