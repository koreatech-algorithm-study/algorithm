'''
baekjoon g5 트리와 쿼리
https://www.acmicpc.net/problem/15681
'''

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
graph = defaultdict(list)

def makeTree(tree: defaultdict, currentNode: int, parent: int) :
    for Node in graph[currentNode] :
        if Node != parent:
            if not tree.get(currentNode):
                tree[currentNode] = {'parent': -1, "child": []}
            if not tree.get(Node):
                tree[Node] = {'parent': -1, "child": []}
            tree[currentNode]['child'].append(Node)
            tree[Node]['parent'] = currentNode
            makeTree(tree, Node, currentNode)

def countSubtreeNodes(size, tree, currentNode) :
    size[currentNode] = 1 # 자신도 자신을 루트로 하는 서브트리에 포함되므로 0이 아닌 1에서 시작한다.
    for Node in tree[currentNode]['child']:
        countSubtreeNodes(size, tree, Node)
        size[currentNode] += size[Node]


N, R, Q = map(int, input().split())
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


tree5 = dict()
makeTree(tree5, R, -1)
size = [0 for _ in range(N+1)]
countSubtreeNodes(size, tree5, R)
for _ in range(Q):
    u = int(input())
    print(size[u])