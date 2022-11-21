# 1744 수 묶기 < 골드 4 >
from sys import stdin

def solution(N, numbers):
    answer = 0
    positive, negative = [], []
    for number in numbers:
        if number > 0:
            positive.append(number)
        else:
            negative.append(number)
    
    positive.sort()
    negative.sort(reverse=True)

    while len(positive) > 1:
        n1, n2 = positive.pop(), positive.pop()
        answer += max(n1 * n2, n1 + n2)
    if positive:
        answer += positive[0]
    
    while len(negative) > 1:
        answer += negative.pop() * negative.pop()
    if negative:
        answer += negative[0]

    return answer

# input
N = int(stdin.readline())
numbers = [int(stdin.readline()) for _ in range(N)]

# result
result = solution(N, numbers)
print(result)