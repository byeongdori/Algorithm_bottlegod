# 7869 - 두 원

import math
x_1, y_1, r_1, x_2, y_2, r_2 = map(float, input().split())

# 먼저 경우 나누고
dis = math.sqrt(pow(x_1 - x_2, 2) + pow(y_1 - y_2, 2))
print(dis)

if dis >= r_1 + r_2:
    print(0)
elif dis < r_1 + r_2 and dis > r_1 - r_2:
    # 여기 다시
    pass
else:
    if r_1 >= r_2:
        print(pow(r_2, 2) * math.pi)
    else:
        print(pow(r_1, 2) * math.pi)