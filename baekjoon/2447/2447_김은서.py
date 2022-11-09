"""
별 찍기 - 10(https://www.acmicpc.net/problem/2447)
"""

import sys

sys.setrecursionlimit(10**6)


def solution(row, col, prev_gap):
    global arr

    if prev_gap == 1:
        return
    curr_gap = prev_gap // 3

    # ① 사각형의 범위 나누기
    for next_row in range(row, row + prev_gap, curr_gap):
        for next_col in range(col, col + prev_gap, curr_gap):
            solution(next_row, next_col, curr_gap)

    # ② 사각형의 빈칸 칠하기
    for blank_row in range(row + curr_gap, row + curr_gap + curr_gap):
        for blank_col in range(col + curr_gap, col + curr_gap + curr_gap):
            arr[blank_row][blank_col] = " "


N = int(input())
arr = [["*" for _ in range(N)] for _ in range(N)]
solution(0, 0, N)
for result in arr:
    print("".join(map(str, result)))
