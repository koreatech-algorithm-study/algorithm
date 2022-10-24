"""
빙산(https://www.acmicpc.net/problem/2573)
"""

from collections import deque


def in_range(row, col, R, C):
    if 0 <= row < R and 0 <= col < C:
        return True
    return False


def solution(R, C, board):
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    year_count = 0  # 2개 이상의 덩어리로 분리되는데 걸리는 시간(년)

    # [1] BFS 탐색 후보(=빙산의 높이가 1 이상인 것) 구하기
    candidates = []
    for row in range(R):
        for col in range(C):
            if board[row][col] > 0:
                candidates.append([row, col])

    while True:
        board_count = 0
        next_board = [[0 for _ in range(C)] for _ in range(R)]
        visited = [[False for _ in range(C)] for _ in range(R)]
        next_candidates = []  # 다음 BFS 탐색 후보

        # [2] candidates에 대해서 BFS 탐색 수행하기
        for row, col in candidates:
            if visited[row][col] or board[row][col] <= 0:
                continue

            # [2-1] 만약 빙산 덩어리가 2개 이상으로 분리되는 경우 => 바로 종료
            board_count += 1
            if board_count >= 2:
                return year_count

            # [2-2] BFS
            queue = deque()
            queue.append([row, col, visited])
            while queue:
                row, col, visited = queue.pop()
                if visited[row][col] or board[row][col] <= 0:
                    continue
                visited[row][col] = True
                zero_count = 0
                for mr, mc in moves:
                    nr = row + mr
                    nc = col + mc
                    if in_range(nr, nc, R, C):
                        if board[nr][nc] <= 0:
                            zero_count += 1
                        if board[nr][nc] > 0 and not visited[nr][nc]:
                            queue.append([nr, nc, visited])

                # [2-3] 상하좌우 중 0의 개수(zero_count)만큼 빼기
                next_board[row][col] = board[row][col] - zero_count

                # [2-4] 뺀 후에도 빙산의 높이가 1 이상인 경우 => 다음 BFS 탐색 후보에 저장하기
                if next_board[row][col] > 0:
                    next_candidates.append([row, col])

        # [3] 만약 모든 얼음이 다 녹아서 빙산 덩어리가 하나도 없는 경우 => 종료
        if board_count == 0:
            return 0
        board = next_board
        candidates = next_candidates
        year_count += 1


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))
result = solution(R, C, board)
print(result)
