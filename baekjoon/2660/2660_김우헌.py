'''
baekjoon g5 회장뽑기
https://www.acmicpc.net/problem/2660
'''
import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
# 2차원 거리테이블 리스트 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자신의 노드간의 거리는 0으로 변경
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
# 주어지는 그래프 정보 입력
while True:
    # a -> b로 가는 비용은 c
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

# k=거쳐가는 노드
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


ans = []
for i in range(1, n+1):
    ans.append(max([k for k in graph[i][1:]]))
min_score = min(ans)
print(min_score, ans.count(min_score))
print(*[index+1 for index, k in enumerate(ans) if k == min_score])