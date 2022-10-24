"""
LCS(https://www.acmicpc.net/problem/9251)
참고: https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence
"""


def solution(s1, s2):
    R = len(s1)
    C = len(s2)
    dp = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(1, R):
        for j in range(1, C):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[R - 1][C - 1]


s1 = " " + input()
s2 = " " + input()
result = solution(s1, s2)
print(result)
