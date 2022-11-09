'''
baekjoon g3 음악프로그램
https://www.acmicpc.net/problem/2623
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
pd_list = []
for _ in range(M):
    p = list(map(int, input()[2:].split()))
    pd_list.append([deque(p), set(p)])

ans = []
visit = set()
for index, _ in enumerate(range(N)):
    for i in list(set([k for k in range(1, N+1)]) - visit):
        flag = True
        # 해당 원소를 순서에 넣을 수 있는지 확인
        for singer_order in pd_list:
            if i in singer_order[1] and singer_order[0][0] != i:
                flag = False
                break
        # 순서에 넣을 수 있다면 순서에 삽입 및 각 순서 목록에서 해당 원소 제거
        if flag:
            ans.append(i)
            visit.add(i)
            for singer_order in pd_list:
                if i in singer_order[1]:
                    singer_order[0].popleft()
                    singer_order[1].remove(i)
            break
    # 이번 반복에서 순서 조건에 맞는 사람을 찾지 못했다면 종료
    if index+1 != len(ans):
        ans = []
        print(0)
        break

for i in ans:
    print(i)
    
        
                    

            

