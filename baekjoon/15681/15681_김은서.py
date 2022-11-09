"""
트리와 쿼리(https://www.acmicpc.net/problem/15681)

풀이
루트(R)부터 리프노드까지 dfs로 탐색하기
→ 만약 더 이상 자식 노드가 없는 리프노드에 도달하면 리턴
→ 리턴되면서 차례대로 현재 노드를 루트로 하는 서브트리와 연결된 노드 수 갱신하기
"""

from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


N, R, Q = map(int, input().split())
graph = defaultdict(set)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

vertex_count = [0 for _ in range(N + 1)]
visited = defaultdict(set)  # 자식 노드 방문 여부를 체크하는 visited


def dfs(node, graph):
    global visited

    children = graph[node]
    total_vertex_count = 1  # total_vertex_count: 현재 node가 루트인 서브트리의 모든 정점의 수
    for child_node in children:
        if child_node not in visited[node]:
            visited[node].add(child_node)
            visited[child_node].add(node)  # 양방향 그래프이므로 반대 경우도 처리해주어야 함
            total_vertex_count += dfs(child_node, graph)

    vertex_count[node] = total_vertex_count

    return total_vertex_count


dfs(R, graph)

for _ in range(Q):
    root = int(input())
    print(vertex_count[root])
