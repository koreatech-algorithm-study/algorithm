"""
과자 나눠주기(https://www.acmicpc.net/problem/16401)
"""

import sys

input = sys.stdin.readline


def solution(M, snacks):
    snacks.sort()

    left = 1
    right = snacks[-1]
    while left <= right:
        mid = (left + right) // 2

        if mid == 0:  # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없다면, 0을 출력
            return 0

        count = 0
        for snack in snacks:
            count += snack // mid

        if count >= M:
            left = mid + 1
        else:
            right = mid - 1

    return right


M, N = map(int, input().split())
snacks = list(map(int, input().split()))
result = solution(M, snacks)
print(result)
