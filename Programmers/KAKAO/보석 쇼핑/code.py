
from collections import deque
from collections import defaultdict
def solution(gems):
    gems_n = len(set(gems))
    min_distance = 100000
    start_point = 0  
    deq = deque()
    jewel_dict = defaultdict(int)
    answer = []
    for end_point in range(len(gems)):
        # answer이 있다면 최소크기만큼 window를 이동
        
# 1
# 윈도우 전체를 움직여 시간복잡도를 조금 줄임
#        if answer:
#            start_point += 1
#            deq.append(gems[end_point])
#            poped_jewel = deq.popleft()
#            jewel_dict[gems[end_point]] += 1
#            jewel_dict[poped_jewel] -= 1
#            if jewel_dict[poped_jewel] == 0:
#                del jewel_dict[poped_jewel]
#        else:
#            deq.append(gems[end_point])
#            jewel_dict[gems[end_point]] += 1
# 2
        deq.append(gems[end_point])
        jewel_dict[gems[end_point]] += 1

        # start_point를 증가 (보석을 다 가지고 있는 경우만 증가)
        if len(jewel_dict) == gems_n:
            while end_point > start_point:
                start_point += 1
                poped_jewel = deq.popleft()
                jewel_dict[poped_jewel] -= 1
                if jewel_dict[poped_jewel] == 0:
                    del jewel_dict[poped_jewel]
                
                if len(jewel_dict) != gems_n:
                    start_point -= 1
                    deq.appendleft(poped_jewel)
                    jewel_dict[poped_jewel] += 1
                    break
                
            if min_distance > end_point-start_point:
                answer = [start_point+1,end_point+1]
                min_distance = end_point-start_point
                
    return answer
