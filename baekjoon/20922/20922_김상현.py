# 20922 겹치는 건 싫어 < 실버 1 >
from sys import stdin
from collections import defaultdict

def solution(N, K, A):
    answer = 0
    left, right = 0, 0

    # [1] 수열에 주어진 각 정수의 개수
    numberCount = defaultdict(int)

    # [2] 투 포인터
    while right < N:
        if numberCount[A[right]] >= K:
            numberCount[A[left]] -= 1
            left += 1
        else:
            numberCount[A[right]] += 1
            right += 1
            answer = max(answer, right - left)
    return answer

# input
N, K = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))

# result
result = solution(N, K, A)
print(result)