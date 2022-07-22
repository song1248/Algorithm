# 몇가지 수가 가능한지
from functools import lru_cache
import copy

def solution(user_ids, banned_ids):
    
    # string이 동일한지 비교('*'은 모든글자에 대응된다)
    def compare(str1, str2):
        for i in range(len(str1)):
            if str1[i] != str2[i] and str2[i] != '*':
                return False
        return True
    
    answer = []
    count_len = len(banned_ids)
    
    # 같은함수 반환
    @lru_cache(None)
    def explore(banned_ids, user_ids, answer_set):
        nonlocal count_len
        nonlocal answer
        banned_ids = list(banned_ids)
        user_ids = list(user_ids)
        answer_set = set(answer_set)
        
        # 재귀함수 탈출조건
        if not banned_ids:
            answer.append(tuple(sorted(answer_set)))
            return
        
        # banned_ids
        for i in range(len(banned_ids)):
            # user_ids
            for j in range(len(user_ids)):
                
                # 복사 및 pop
                copied_banned_ids = copy.deepcopy(banned_ids)
                poped_banned_id = copied_banned_ids.pop(i)
                copied_user_ids = copy.deepcopy(user_ids)
                poped_user_id = copied_user_ids.pop(j)
                
                # 사용할 banned_ids와 user_ids의 길이가 다르면 종료
                if len(poped_banned_id) != len(poped_user_id):
                    continue
                
                # 사용할 banned_ids와 user_ids가 다르면 종료
                if not compare(poped_user_id, poped_banned_id):
                    continue
                
                # 새로운 입력에 넣어주기위해 copy
                tmp_answer_set = copy.deepcopy(answer_set)
                tmp_answer_set.add(poped_user_id)
                
                explore(tuple(copied_banned_ids), tuple(copied_user_ids), tuple(tmp_answer_set))

    
    explore(tuple(banned_ids), tuple(user_ids), tuple(set()))
    return len(set(answer))
