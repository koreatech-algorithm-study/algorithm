'''
baekjoon g3 소문난 칠공주
https://www.acmicpc.net/problem/1941
'''
import sys


def solution(school_class: list):
    cases = set()
    def dfs(y_count: int, depth: int, case: list):
        if y_count > 3:
            return
        if depth == 7:
            case.sort()
            cases.add(tuple(case))
            return

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for x, y in case:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x+dx, y+dy
                if 0 <= nx <= 4 and 0 <= ny <= 4 and (nx, ny) not in case:
                    if school_class[nx][ny] == 'Y':
                        dfs(y_count+1, depth+1, case+[(nx, ny)])
                    else:
                        dfs(y_count, depth + 1, case + [(nx, ny)])

    for r in range(5):
        for c in range(5):
            if school_class[r][c] == 'S':
                dfs(0, 1, [(r, c)])

    return len(cases)


input = sys.stdin.readline

school_class = []
for r in range(5):
    cols = list(input().strip())
    school_class.append(cols)

print(solution(school_class))
