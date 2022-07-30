# 외벽의 길이 n
# 수리지점 weak
# 한시간동안 이동할 수 있는 거리

# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값(모두 점검할 수 없는경우 -1)

# greedy

# 완전탐색
# 가장 큰 길이부터 개수를 늘려가며 탐색
# 가장 큰길이 n개 가 있을때 가장 작은 길이가 최대 개수를 커버하도록 탐색 진행
from itertools import permutations
from collections import deque
import copy

def solution(n, weak, dist):
    
    # 탐색 함수 정의
    # start point와 일하는 친구의 수가 주어졌을때 최솟값을 구하는 함수
    def explore(weak, friends_n):
        
        # permutations 조합 수하기
        friends_combi = list(permutations(dist[:friends_n], friends_n))
        
        # 첫 위치를 0 으로 weak point의 거리를 재설정
        weak_list = deque()
        start_point = weak[0]
        for i in weak:
            weak_list.append( (i + n - start_point)%n )      
        
        # 조합 뽑아내기 
        for combi in friends_combi:
            # weak_list 복사
            tmp_weak_list = copy.deepcopy(weak_list)
            # 일할 친구
            for friend_dist in combi:
                # 점검을 시작하는 위치는 벽이 손상된 위치
                cur_point = tmp_weak_list[0]+friend_dist
                # 현재 일을하는 친구가 최대 점검할 수 있는 point까지 pop
                while tmp_weak_list:
                    if cur_point < tmp_weak_list[0]:
                        break
                    tmp_weak_list.popleft()
                # 모든 weak_point를  점검했으면 True 를 return
                if not tmp_weak_list:
                    return True
        # 모든 weak_point를  점검하지 못했으면 False 를 return  
        return False    
    
    weak = deque(weak)
    
    # 많은 장소를 점검할 수 있는 순으로 정렬)(greedy)
    dist.sort(reverse=True)

    # 친구수 weak_point의 수 만큼반복
    for friends_n in range(len(dist)):
        friends_n += 1 
        # 회전시켜가며, 첫 위치를 변경하며 탐색
        for _ in range(len(weak)):
            poped = weak.popleft()
            weak.append(poped)
            if explore(weak, friends_n):
                return friends_n

    return -1
