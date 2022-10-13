# 15486 퇴사 2 < 골드 5 >
from sys import stdin

def solution(N,TP):
    dp = [0] * (N + 2) # dp 배열

    for day in range(N,0,-1): # 마지막날(N)부터 시작
        term, pay = TP[day]
        # day날에 해당하는 상담이 종료하는 날이 퇴사하는 날(N) 전이라면
        if day + term <= N + 1:
            
            # day날에 시작하는 상담이 종료되는 날의 pay와  
            dp[day] = max(dp[day + term] + pay, dp[day + 1])
        else:
            dp[day] = dp[day + 1]
    return max(dp)

N = int(stdin.readline())
TP = [0]+[list(map(int,stdin.readline().split())) for _ in range(N)]

print(solution(N,TP))