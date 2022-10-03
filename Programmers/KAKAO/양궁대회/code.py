
from functools import lru_cache

def solution(n, info):
    
    lion_socre = [ 0 for _ in range(11)] 
    tmp_list = []
    
    # 라이언이 쏠 수 있는 모든경우 
    @lru_cache(None)
    def exp_val(n, lion_socre):
        nonlocal tmp_list
        
        tmp = []
        lion_socre = list(lion_socre)
        get_point = False;
        
        # 가능한 것들 탐색
        for idx, point in enumerate(info):
            if point < n and lion_socre[idx] == 0:
                get_point = True
                tmp_lion_socre = lion_socre.copy()
                tmp_lion_socre[idx] = point + 1
                tmp.extend((exp_val(n-(point+1), tuple(tmp_lion_socre))))
                        
        # 갈곳이 없으면
        if tmp:
            return tmp
        else:
            lion_socre[-1] += n
            return [lion_socre]
    
    max_score = 0
    answer_list = []
    
    # 가능한 score_list 중에서
    a = list(exp_val(n = n, lion_socre = tuple(lion_socre)))

    for score_list in a:
        l_score = 0
        a_score = 0
        for i in range(11) :
            if score_list[i] > info[i]:
                l_score += 10 - i
            if score_list[i] <= info[i] and info[i] > 0:
                a_score += 10 - i
        
        # 가장 작은거의 개수
        count = []
        for i in range(10,-1,-1):
            if score_list[i] != 0:
                count = [-i ,-score_list[i]]
                break
        
        # 라이언이 이기는 경우를 탐색
        if l_score - a_score > max_score:
            answer_list = [count + score_list]
            max_score = l_score - a_score
        elif l_score - a_score == max_score and max_score != 0:
            answer_list.append(count + score_list)
    
    return sorted(answer_list, key = lambda x :(x[0], x[1]))[0][2:] if answer_list else [-1]
