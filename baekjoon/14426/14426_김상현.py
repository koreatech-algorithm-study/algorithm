# 14426 접두사 찾기 < 실버 2 >
from sys import stdin

def solution(S, words):
    answer = 0
    for word in words:
        for s in S:
            if s.startswith(word):
                answer += 1
                break
    return answer

# input
N, M = map(int,stdin.readline().split())
S = [stdin.readline().rstrip() for _ in range(N)]
words = [stdin.readline().rstrip() for _ in range(M)]

# result
result = solution(S, words)
print(result)