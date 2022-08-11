# abbb같은 경우도 있을 수 있다
def solution(s):
    answer = 1
    for i in range(1,len(s)):
        # 중앙이 짝수인경우
        count = 0
        for j in range(i):
            if i+j >= len(s) or i-1-j<0:
                break
            if s[i+j] == s[i-1-j]:
                count += 2
            else:
                break
        answer = max(count, answer)
        
        # 중앙이 홀수인 경우
        count = 1
        for j in range(i):   
            if i+j+1 >= len(s) or i-j-1 < 0:
                break
            if s[i+j+1] == s[i-j-1]:
                count += 2
            else:
                break
        answer = max(count, answer)
        
    return answer
