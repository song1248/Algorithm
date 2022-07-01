import copy
def solution(name):
    
    # 이름을 이동횟수 list로 바꾸기
    name = [ min(ord(x) - 65, 26 - (ord(x) - 65)) for x in name]
    answer = sum(name)
    answer_list = []
    
    # 모든 경우의 수 중 비용이 가장 작은 경우의 수 고르기
    # 0이 아닌 수를 만날때 까지의 거리를 구해서 가까운 곳으로 이동
    # 도착한곳을 0으로 바꿈
    # 모든곳이 0이 되면 종료
    def move_point(name,answer,i=0):
        nonlocal answer_list
        name = copy.deepcopy(name)
        name[i] = 0
        
        if sum(name) == 0:
            return answer_list.append(answer)
        
        # 오른쪽 으로 이동
        r_index = i
        r_distance = 0
        while name[r_index] == 0:
            r_index = (r_index + 1 + len(name))%len(name)
            r_distance += 1
        move_point(name,answer+r_distance,r_index)
        
        # 왼쪽 으로 이동
        l_index = i
        l_distance = 0
        while name[l_index] == 0:
            l_index = (l_index - 1 + len(name))%len(name)
            l_distance += 1      
        move_point(name,answer+l_distance,l_index)
        
    move_point(name,answer)
       
    return min(answer_list)
