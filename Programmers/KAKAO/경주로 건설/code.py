from collections import deque
import heapq
import copy

def solution(board):
    
    # 이전 방향이 상 하 좌 우
		# 3차원 DP생성
    boards = [ copy.deepcopy(board) for _ in range(4) ] 
    
    # board에 cost를 갱신해가며 bfs
		# 시간복잡도를 줄이기위해 heapq를 이용
    heap = []
    # i=0, j=0, cost=0, prv_direction=[2,2])
    heapq.heappush(heap, ( -500, 0, 0, [2,2]))
    
    # 상 하 좌 우
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    
    answer = float('inf')
    while heap:
        poped = heapq.heappop(heap)
        cur_cost = poped[0]
        cur_i = poped[1]
        cur_j = poped[2]
        prv_direction = poped[3]
        board_idx = 0
        
				# 이전 방향에따라 어떤 dp를 사용할지 선택
        for i, d in enumerate(directions):
            if d == prv_direction:
                board_idx = i
        
        # 범위 벗어나면 탐색안함
        if cur_i<0 or cur_j<0 or cur_i>=len(board) or cur_j>=len(board[0]):
            continue
            
        # board update:
        # (현재 cost가 board의 cost보다 작거나 board의 cost가 0 이)이 아니면 continue
        if boards[board_idx][cur_i][cur_j] != 0 and boards[board_idx][cur_i][cur_j] < cur_cost:
            continue
        
        # update
				# 이 전 방향에따라 각기 다른 dp에 업데이트
        boards[board_idx][cur_i][cur_j] = cur_cost    
        
        # print(cur_i,cur_j)
        # print([len(board)-1, len(board[0])-1])
        # print(cur_cost)
        # for k in  boards:
        #     print(k)        

        # 도착지에 도달했을 경우
        if [cur_i, cur_j] == [len(board)-1, len(board[0])-1]:
            answer = min(cur_cost, answer)
            # print(cost)
            break 
        
        # 갈 수 있는 방향으로 탐색
        # 이동시 += 100
        # 다른 방향이면 += 500
        cur_cost += 100
        for d, cur_direction in enumerate(directions):
            dy = cur_direction[0]
            dx = cur_direction[1]
            # 이전 방향과 같은 방향이면
            if prv_direction == cur_direction:
                heapq.heappush(heap,( cur_cost, cur_i+dy, cur_j+dx, cur_direction))
            # 이전 방향의 뒷 방향이면
            elif list(map(lambda x: -x ,prv_direction)) == cur_direction:
                continue
            # 다른방향의 경우
            else:
                heapq.heappush(heap,( cur_cost+500, cur_i+dy, cur_j+dx, cur_direction))

    return answer
