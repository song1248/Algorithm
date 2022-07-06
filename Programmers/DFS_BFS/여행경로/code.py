import copy
def solution(tickets):
    
    tickets.sort(key = lambda x : x[1])
    used = [0 for _ in tickets]
    # 갈 수 있는 곳으로 이동 성공한다면
    answer = []
    
    def travel_path(ticket_num=-1, used=used, path=['ICN']):
        nonlocal answer
        # 방문처리 & path에 추가
        if ticket_num != -1:
            used[ticket_num] = 1
            path.append(tickets[ticket_num][1])
            
        # 종료조건
        if answer:
            return
        
        # answer 만들기(정렬 후 dfs를 진행하였기 때문에 첫번째 도달한 answer이 답이다)
        if sum(used) == len(used):
            answer = path
            return
            
        departure = path[-1]

        for ticket_num, ticket in enumerate(tickets):
            ticket_departure = ticket[0]
            ticket_destination = ticket[1]
            if ticket_departure == departure and used[ticket_num] == 0:
                new_used = copy.deepcopy(used)
                new_path = copy.deepcopy(path)
                travel_path(ticket_num, new_used ,new_path)
    
    travel_path()
    return answer
