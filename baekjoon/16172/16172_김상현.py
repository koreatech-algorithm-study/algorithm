# 16172 나는 친구가 적다 < 브론즈 2 >
from re import findall
from sys import stdin

def solution(S, K):
    # 문자열 K가 문자열 S에서 숫자를 제외한 문자열에 연속으로 일치할 경우
    if K in ''.join(findall("[a-zA-Z]", S)):
        return 1
    else:
        return 0

# input
S = stdin.readline().strip()
K = stdin.readline().strip()

# result
result = solution(S, K)
print(result)