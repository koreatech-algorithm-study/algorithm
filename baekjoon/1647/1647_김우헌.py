'''
baekjoon g4 도시 분할 계획
https://www.acmicpc.net/problem/1647
'''

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

# 부모 노드 정보:
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선 정보
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

total_cost = []
for i in range(M):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost.append(cost)

print(sum(total_cost[:len(total_cost)-1]))



