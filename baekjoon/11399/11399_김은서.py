"""
ATM(https://www.acmicpc.net/problem/11399)
"""

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = 0
for i in range(N):
    for j in range(0, i + 1):
        result += nums[j]
print(result)
