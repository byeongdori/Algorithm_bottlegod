# 9012 - 괄호

def check_vaild_paren(str):
    count = 0
    for i in range(len(str)):
        if str[len(str) - i - 1] == ")":
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return print("NO")
    if count == 0:
        return print("YES")
    else:
        return print("NO")

case = int(input())

for i in range(case):
    input_list = input()
    check_vaild_paren(input_list)