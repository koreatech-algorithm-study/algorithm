"""
연산자 끼워넣기(https://www.acmicpc.net/problem/14888)
풀이방법: 
"""


def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2

    if op == "-":
        return num1 - num2

    if op == "*":
        return num1 * num2

    if op == "/":
        if num1 < 0:
            return -((-num1) // num2)
        return num1 // num2


def solution(N, numbers, operators):
    op = {
        0: "+",
        1: "-",
        2: "*",
        3: "/",
    }

    def calculator(i, result, operators):
        if i == N:  # 모든 숫자를 다 사용하면(i==N) 현재까지의 계산값 리턴
            return [result, result]

        max_number = -float("inf")
        min_number = float("inf")
        curr_number = numbers[i]
        for j, cnt in enumerate(operators):
            if cnt > 0:
                next_number = calculate(result, curr_number, op[j])
                operators[j] -= 1  # 연산자 사용 후 개수 -1
                max_result, min_result = calculator(i + 1, next_number, operators)  # 최댓값, 최솟값 갱신
                operators[j] += 1

                max_number = max(max_number, max_result)
                min_number = min(min_number, min_result)

        return [max_number, min_number]

    max_result, min_result = calculator(1, numbers[0], operators)
    return [max_result, min_result]


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
result = solution(N, numbers, operators)
print(result[0])
print(result[1])
