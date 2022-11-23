'''
baekjoon g1 멀티탭 스케줄링
https://www.acmicpc.net/problem/1700
'''

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, K = map(int, input().split())
use_list = list(map(int, input().split()))
electronic_using_dict = defaultdict(deque)
for index, use in enumerate(use_list):
    electronic_using_dict[use].append(index)

plug = []
ans = 0
for use in use_list:
    if use in plug:
        electronic_using_dict[use].popleft()
        continue
    if len(plug) == N:
        max_next_index = -1
        out_plug_index = -1
        for index, p in enumerate(plug):
            if not electronic_using_dict[p]:
                out_plug_index = index
                break
            elif electronic_using_dict[p][0] > max_next_index:
                max_next_index = electronic_using_dict[p][0]
                out_plug_index = index
        del plug[out_plug_index]
        ans += 1
    plug.append(use)
    electronic_using_dict[use].popleft()

print(ans)