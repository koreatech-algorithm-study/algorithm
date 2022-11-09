# 15681 트리와 쿼리 < 골드 5 >
from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**6) # 최대 재귀 깊이의 값을 10^6 으로 재설정

def solution(N, R, UV, U):

    connect = defaultdict(list)
    parents = list(range(N+1))
    tree = defaultdict(list)
    size = list(0 for _ in range(N+1))

    # 연결 관계 초기화
    for u, v in UV:
        connect[u].append(v)
        connect[v].append(u)

    # 각 정점을 루트로 하는 서브트리에 속한 정점의 수 count
    def countSubtreeNodes(currentNode) :
        size[currentNode] = 1 # 자신도 자신을 루트로 하는 서브트리에 포함되므로 0이 아닌 1에서 시작한다.
        for Node in tree[currentNode]:
            countSubtreeNodes(Node)
            size[currentNode] += size[Node]

    # R을 정점으로 하는 트리 생성
    def makeTree(currentNode, parent) :
        for Node in connect[currentNode] :
            if Node != parent:
                #add Node to currentNode’s child
                tree[currentNode].append(Node)
                #set Node’s parent to currentNode
                parents[Node] = currentNode
                makeTree(Node, currentNode)
        

    makeTree(R,-1)
    countSubtreeNodes(R) 

    # 정점 u를 루트로 하는 서브트리에 속한 정점의 수 출력
    for u in U:
        print(size[u])

N, R, Q = map(int,stdin.readline().split())
UV = list(list(map(int,stdin.readline().split())) for _ in range(N-1))
U = list(int(stdin.readline()) for _ in range(Q))

solution(N, R, UV, U)