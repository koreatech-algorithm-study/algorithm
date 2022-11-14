"""
접두사 찾기(https://www.acmicpc.net/problem/14426)
"""


def solution(target_words, check_words):
    # [1] 가능한 접두사 후보들을 모두 만들어서 저장하기
    candidates = set()
    for target_word in target_words:
        curr_word = ""
        for i in range(len(target_word)):
            curr_word += target_word[i]
            candidates.add(curr_word)

    # [2] 문자열이 접두사 후보에 포함되어 있는지 확인하기
    answer = 0
    for check_word in check_words:
        if check_word in candidates:
            answer += 1

    return answer


N, M = map(int, input().split())
target_words = []  # 집합에 포함된 문자열
for _ in range(N):
    target_words.append(input())

check_words = []  # 검사해야 되는 문자열
for _ in range(M):
    check_words.append(input())

result = solution(target_words, check_words)
print(result)
