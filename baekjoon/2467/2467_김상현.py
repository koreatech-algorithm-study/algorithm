from sys import stdin, maxsize

def solution(N,solution_list):
    answer = [maxsize, 0, 0] # 특성값, 용액1, 용액2
    start, end = 0, N-1 # 시작 인덱스, 끝 인덱스

    while start < end:
        # 두 용액을 혼합한 특성값
        avg = solution_list[start] + solution_list[end]

        # 두 용액을 혼합한 특성값(avg)이 0에 가장 가까운 경우
        if answer[0] > abs(avg):
        	# answer 갱신
            answer = [abs(avg), solution_list[start], solution_list[end]]
        
        # 두 용액을 혼합한 특성값에 따라 용액 교체
        if avg < 0: start += 1 
        else: end -= 1

    return answer[1], answer[2]

N = int(stdin.readline())
solution_list = list(map(int,stdin.readline().split()))
s1, s2 = solution(N,solution_list)
print(s1, s2)