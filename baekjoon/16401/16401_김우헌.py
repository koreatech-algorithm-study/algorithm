'''

'''

import sys


def solution(M, snacks):
    result = 0
    start = 0
    end = max(snacks)
    while start <= end:
        mid = (start + end) // 2
        div = sum([snack // mid for snack in snacks])
        if div >= M:
            start = mid + 1
            result = mid
        elif div < M:
            end = mid - 1
    return result

input = sys.stdin.readline
M, N = map(int, input().split())
snacks = list(map(int, input().split()))
snacks.sort()
print(solution(M, snacks))
