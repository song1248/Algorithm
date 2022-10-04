
# 후보키의 개수

# 학번 이름 전공 학년 의 조합중

# 유일성 : 유일성

# 최소성 :  릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

# 모든 후보키를 구하고 -> 최소성을 만족하도록한다

from itertools import combinations

def solution(relation):
    
    len_col = len(relation[0])
    len_row = len(relation)
    
    # step 1 : 가능한 조합 구하기
    com_list =[]
    for i in range(1,len_col+1):
        com_list.extend(list(combinations(list(range(0,len_col)), i)))
    
    # step 2 : 가능한 조합별로 묶어서 보았을떄 유일성을 만족하면 answer_list에 추가
    answer_list =[]
    # 조합별로
    for combi in com_list:
        relation_set = set()
        # 사람별로
        for row in range(len_row):
            tmp_string =''
            # 조합리스트
            for col in combi:
                tmp_string += relation[row][col]
            relation_set.add(tmp_string)
        if len(relation_set) == len_row:
            answer_list.append(combi) 
            
    # 길이가 작은순으로 sort(시간복잡도를 줄이기 위함)
    answer_list = sorted(answer_list, key = lambda x : len(x))
    
    # step 3 : 가능한 조합에서 더 작은것을 포함하고있는 combi 제거
    i = 0    
    tmp_len = len(answer_list)
    while i < tmp_len-1:
        answer_list = list(filter(lambda x : ((answer_list[i] == x) or (len(set(answer_list[i]) - set(x)) != 0)) , answer_list))
        
        # 지워진것이 없으면
        if tmp_len == len(answer_list):
            i += 1    
        tmp_len = len(answer_list)


    return len(answer_list)
