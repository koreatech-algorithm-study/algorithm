'''
baekjoon g5 용약
https://www.acmicpc.net/problem/2467
모든 n에 대해 합쳐서 0이되는 경우를 이진탐색으로 찾기
0이안되면 0과 가장 가까운 값이 되는 경우?
'''

import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

mixed = []
flag = False
for num in num_list:
    nearby = (0, 0, float('inf'))
    start, end = 0, N-1
    while start <= end:
        mid = (end+start) // 2
        if num != num_list[mid]:
            # 현재 mid값으로 용액 생성
            small, big = min(num, num_list[mid]), max(num, num_list[mid])
            curr = (small, big, abs(num + num_list[mid]))
            if curr[2] < nearby[2]:
                nearby = curr
                if nearby[2] == 0:
                    flag = True
                    break
        if -num > num_list[mid]:
            start = mid + 1                  
        elif -num < num_list[mid]:
            end = mid - 1
        else:
            break
            
    mixed.append(nearby)
    if flag:
        break
        
mixed.sort(key = lambda x : x[2])
print(mixed[0][0], mixed[0][1])