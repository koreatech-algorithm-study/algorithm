# 16401 과자 나눠주기 < 실버 2 >
from sys import stdin

# M명의 조카에게 줄 수 있는 막대 과자의 최대 길이
def solution(M, N, L):
    
    # mid 길이로 만들 수 있는 막대 과자 개수
    def check(mid):
        cnt = 0
        for length in L:
            cnt += length//mid
        return cnt

    # 시작과 끝 값
    start, end = 1, max(L)

    # 이진 탐색
    while start <= end:
        mid = (start + end) // 2
        if check(mid) >= M:
            start = mid+1
        else:
            end = mid-1
        
    return end

# input
M, N = map(int,stdin.readline().split())
L = sorted(list(map(int,stdin.readline().split())))

# result
result = solution(M, N, L)
print(result)