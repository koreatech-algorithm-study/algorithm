# 16987 계란으로 계란치기 < 실버 1 >
from sys import stdin

# input
N = int(stdin.readline())
eggs = [list(map(int,stdin.readline().split())) for _ in range(N)]
result = 0

def countCrackedEggs(eggs):
    global result
    cnt = 0
    for egg in eggs:
            if egg[0] <= 0:
                cnt += 1
    result = max(result, cnt)

def solution(sequence, eggs):
    global result
    # [1] 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료
    if sequence == N:
        countCrackedEggs(eggs)
        return

    # [2] 손에 든 계란이 깨진 상태
    if eggs[sequence][0] <= 0:
        solution(sequence+1, eggs)
        return

    # [3] 깨지지 않은 다른 계란이 없는 상태
    check = True
    for i in range(N):
        if sequence == i: continue
        if eggs[i][0] > 0: check = False
    if check:
        countCrackedEggs(eggs)
        return

    # [4] 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다
    for i in range(N):
        if i == sequence: continue
        if eggs[i][0] <= 0: continue
        # crash
        eggs[sequence][0] -= eggs[i][1]
        eggs[i][0] -= eggs[sequence][1]
        solution(sequence+1,eggs)
        # recover
        eggs[sequence][0] += eggs[i][1]
        eggs[i][0] += eggs[sequence][1]

# result
solution(0, eggs)
print(result)