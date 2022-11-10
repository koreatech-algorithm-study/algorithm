# 7795 먹을 것인가 먹힐 것인가 < 실버 3 >
from sys import stdin
from bisect import bisect_left
def solution(A,B):
    answer = 0
    for a in A:
        answer += bisect_left(B,a)
    return answer

# input
T = int(stdin.readline())
for _ in range(T):
    N, M = map(int,stdin.readline().split())
    A = sorted(list(map(int,stdin.readline().split())))
    B = sorted(list(map(int,stdin.readline().split())))

    # result
    result = solution(A,B)
    print(result)