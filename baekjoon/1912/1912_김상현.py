# 1912 연속합 < 실버 2 >
from sys import stdin

def solution(N,nums):
    # [1] 누적합을 구한다.
    for i in range(1,N):
        nums[i] = max(nums[i], nums[i] + nums[i-1])
    return max(nums)

# input
N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

# result
result = solution(N,nums)
print(result)