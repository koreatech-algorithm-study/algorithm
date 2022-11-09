"""
퇴사(https://www.acmicpc.net/problem/15486)
풀이: dp
"""

import sys

input = sys.stdin.readline


def solution(N, schedule):
    dp = [0 for _ in range(N + 1)]
    for i, [day, profit] in enumerate(schedule):
        if i + day <= N:
            dp[i + day] = max(dp[i] + profit, dp[i + day])  # i일에 상담을 하는 경우 & 안하는 경우 비교
        dp[i + 1] = max(dp[i], dp[i + 1])  # 이익은 계속 누적되므로 값을 갱신시켜야 함

    return dp[-1]


N = int(input())
schedule = []
for _ in range(N):
    schedule.append(list(map(int, input().split())))
result = solution(N, schedule)
print(result)
