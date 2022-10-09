'''
https://www.acmicpc.net/problem/15486
'''
from sys import stdin

def solution(day, arr):
    dp = [0] * (n + 1)
    for d, tp in enumerate(arr):
        t, p = tp
        dp[d] = max(dp[d], dp[d-1])
        if t + d <= day:
            dp[d + t] = max(dp[d] + p, dp[d + t])
    return max(dp[day-1], dp[day])

if __name__ == '__main__':
    n = int(stdin.readline())
    arr = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    result = solution(n, arr)
    print(result)

