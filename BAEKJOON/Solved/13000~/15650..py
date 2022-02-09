# 15650 - N과 M(2)
# 백트레킹

n, m = map(int,input().split())

result = []

def back_tracking(current, n, m_local):
    
    if m_local == m:
        print(*result)
        return

    for i in range(current, n + 1):
        result.append(i)
        back_tracking(i + 1, n, m_local + 1)
        result.pop()

back_tracking(1, n, 0)