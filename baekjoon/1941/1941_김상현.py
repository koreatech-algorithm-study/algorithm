# 1941 소문난 칠공주 < 골드 3 >
from sys import stdin

def solution(table):
    cases = set() # ‘소문난 칠공주’ 결성 cases

    def dfs(case, depth, cntY):
        # 임도연파 학생이 과반수 이상일 경우
        if cntY > 3:
            return

        # 7명의 구성이 완성되었을 경우
        if depth == 7:
            cases.add(tuple(sorted(case)))
            return

        # 모든 경우의 수를 탐색(dfs)
        for x, y in case:
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx > 4 or ny < 0 or ny > 4 or (nx,ny) in case: continue
                if table[ny][nx] == 'Y':
                    dfs(case + [(nx,ny)], depth + 1, cntY + 1)
                else:
                    dfs(case + [(nx,ny)], depth + 1, cntY)
    
    for y in range(5):
        for x in range(5):
            if table[y][x] == 'S':
                dfs([(x,y)], 1, 0)
        
    return len(cases)

table = [list(stdin.readline().strip()) for _ in range(5)]
result = solution(table)
print(result)