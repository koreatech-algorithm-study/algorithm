'''
baekjoon g4 운동
https://www.acmicpc.net/problem/1956
'''
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
# 2차원 거리테이블 리스트 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 주어지는 그래프 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# k=거쳐가는 노드
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = INF
for i in range(1, n+1):
    ans = min(ans, graph[i][i])
print(ans if ans < INF else -1)