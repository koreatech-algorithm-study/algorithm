"""
용액(https://www.acmicpc.net/problem/2467)
풀이: 투포인터
"""


def solution(N, numbers):
    minimum_value = float("inf")  # 특성값의 절댓값
    left, right = 0, N - 1
    answer = []
    while left < right:
        sum = numbers[left] + numbers[right]
        if abs(sum) <= minimum_value:  # 특성값의 절댓값이 작을수록 0에 가까움
            minimum_value = abs(sum)
            answer = [numbers[left], numbers[right]]
        if sum < 0:  # 특성값이 음수이면 left를 오른쪽으로 이동시켜서 sum을 크게 만듦
            left += 1
        else:  # 특성값이 양수이면 right를 왼쪽으로 이동시켜서 sum을 작게 만듦
            right -= 1

    return answer


N = int(input())
numbers = list(map(int, input().split()))
result = solution(N, numbers)
print(" ".join(map(str, result)))
