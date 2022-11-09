# 2660 회장뽑기 < 골드 5 >
from sys import stdin
from collections import defaultdict

def solution(N, edges):
    ranking = defaultdict(list) # { 점수(key) : 회원 번호(value) }

    # 모든 회원 점수 검색
    for i in range(1,N+1):
        point = 0 # 회원 점수
        connection = edges[i] # i번째 회원 친구
        visited = [True] + [False] * N # i번째 회원 친구 관계
        visited[i] = True

        # 모든 회원과 친구 관계가 될때까지 반복
        while not all(visited): 
            tmp = [] # 친구의 친구 관계를 저장할 리스트
            point += 1
            # 현재 회원의 친구 관계에 해당하는 모든 회원 조회
            for node in connection: 
                visited[node] = True # 친구 관계 설정
                # 친구의 친구 관계 tmp에 저장
                for nextNode in edges[node]:
                    if not visited[nextNode]:
                        tmp.append(nextNode)
            # connection을 친구의 친구 관계로 갱신
            connection = tmp
        ranking[point].append(i)
    
    score = min(ranking.keys()) # 회장 후보의 점수
    candidates = sorted(ranking[score]) # 회장 후보

    return score, candidates

# input
edges = defaultdict(list)
N = int(stdin.readline())
while True:
    member1, member2 = map(int,stdin.readline().split())
    if member1 == -1 and member2 == -1:
        break
    edges[member1].append(member2)
    edges[member2].append(member1)

# answer
score, candidates = solution(N, edges)
print(score, len(candidates))
for candidate in candidates: print(candidate,end=' ')