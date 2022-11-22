# 20922 겹치는 건 싫어 < 실버 1 >
from sys import stdin
from collections import defaultdict

def solution(N, K, A):
    answer = 0
    start, end = 0, 0

    # [1] 수열에 주어진 각 정수의 개수
    numberCount = defaultdict(int)

    # [2] 투 포인터
    while end < N:
        if numberCount[A[end]] >= K:
            numberCount[A[start]] -= 1
            start += 1
        else:
            numberCount[A[end]] += 1
            end += 1
            answer = max(answer, end - start)

    return answer

# input
N, K = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))

# result
result = solution(N, K, A)
print(result)