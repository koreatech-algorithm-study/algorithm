'''
https://www.acmicpc.net/problem/2467
투포인터
'''

from sys import stdin

def solution(n ,arr):
    i = 0
    j = len(arr)-1
    pre = [abs(arr[i] + arr[j]), (arr[i], arr[j])]
    while i < j:
        tmp = arr[i] + arr[j]
        if abs(tmp) < pre[0]:
            pre = [abs(arr[i] + arr[j]), (arr[i], arr[j])]
        if tmp > 0: j -= 1
        elif tmp < 0: i += 1
        else: return pre[1]
    return pre[1]


n = int(input())
arr = list(map(int, stdin.readline().split(' ')))
near = solution(n, arr)
print(near[0], near[1])
