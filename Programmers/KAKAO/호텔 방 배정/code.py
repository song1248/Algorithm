from collections import defaultdict

# 방이 총 k개 있으며, 각각의 방은 1번부터 k번까지 번호로 구분하고 있습니다.
# 1. 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
# 2. 고객은 투숙하기 원하는 방 번호를 제출합니다.
# 3. 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
# 4. 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.

def solution(k, room_numbers):
    
    Ddict = defaultdict(list)
    
    
    for customer_number, room_number in enumerate(room_numbers):
        
        # target_node를 room_number 초기화
        target_node = room_number
        throught_node = set()
        
        # Ddict에 room_number가 없으면 있을때까지 찾기
        while Ddict[target_node]:
            throught_node.add(target_node)  # 거쳐간 node stack에 추가
            target_node = Ddict[target_node][1]  # target_node를 현재 node가 가르키는 node로 재설정
        
        # Ddict[target_node] 초기화
        Ddict[target_node] = [set(), target_node, customer_number + 1]
        
        # 현재 node stack에 추가
        throught_node.add(target_node)
        
        # stack을돌며 가르키는 node를 target node+1 로 변경
        for i in throught_node:
            Ddict[i][1] = target_node + 1
        
        # Ddict[target_node]의 자신을 가르키는 노드들 추가
        Ddict[target_node][0] = throught_node | Ddict[target_node][0]

    answer = []
    for room_number in Ddict.keys():  # key는 dictionary의 key가 생성된 순서대로 만들어진다
        answer.append(room_number)
        
    return answer
