'''
baekjoon g5 퇴사 2
https://www.acmicpc.net/problem/15486
'''

import sys

input = sys.stdin.readline

N = int(input())
counseling_set = []
benefit = [0] * (N+1)
for i in range(N):
    T, P = map(int, input().split())
    counseling_set.append([T, P])

for i, [day, profit] in enumerate(counseling_set):
    if i + day <= N:
        benefit[i+day] = max(benefit[i] + profit, benefit[i+day])
    benefit[i+1] = max(benefit[i], benefit[i+1])

print(benefit[-1])