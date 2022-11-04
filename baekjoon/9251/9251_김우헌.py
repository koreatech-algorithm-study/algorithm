'''
baekjoon g5 lcs
https://www.acmicpc.net/problem/9251
'''
import sys

input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()
LCS = [[0 for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]
for i in range(1, len(S1)+1):
    for j in range(1, len(S2)+1):
        if S1[i-1] == S2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

ans = max([max(i) for i in LCS])
print(ans)
