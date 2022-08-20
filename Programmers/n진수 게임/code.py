# 진법 n
# 구할 숫자의 개수 t
# 게임에 참가하는 인원  m
# 튜브의 순서 p

def solution(n, t, m, p):
    
    # n_진수계산 함수
    def n_number(n, num):
        # 예외처리
        if num == 0:
            return ['0']
        
        # mok : 몫
        # namuge : 나머지
        digit_list = []
        for digit in range(12, -1, -1):
            if not digit_list and n**digit > num:
                continue
            else:
                mok = num // n**digit
                namuge = num % n**digit
                digit_list.append(hex(mok)[2:])
                num = namuge
        
        return digit_list
    
    # n_진수 변환하여 num_list에 추가
    num_list = []
    cur_num = 0 
    while len(num_list) <= m*(t):
        num_list.extend(n_number(n, cur_num))
        cur_num += 1
    
    # num_list에서 튜브가 말해야되는 idx의 값 answer에 추가
    answer = ''
    for i in range(0, t):
        answer += num_list[i*m+p-1].upper()
        
    return answer
