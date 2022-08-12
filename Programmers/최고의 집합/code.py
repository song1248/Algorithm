def solution(n, s):
    # 자연수 n 개로 이루어진 중복집합
    # 합이 S 가 되고 곱이 최대가 되는 집합
    if n > s:
        return [-1]
    
    num = s // n
    auxiliary_num = 0
    while num * n + auxiliary_num != s:
        auxiliary_num += 1
    
    answer = [ num  for _ in range(n)  ]
    for i in range(auxiliary_num):
        answer[i] += 1
    
    answer.sort()
    return answer
