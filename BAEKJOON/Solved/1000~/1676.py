# 팩토리얼 0의 개수

n = int(input())

result = 0
result += n // 5
result += n // 25
result += n // 125
print(result)