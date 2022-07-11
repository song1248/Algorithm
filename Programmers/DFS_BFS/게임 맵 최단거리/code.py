from collections import deque

def solution(maps):
    answer = 0
    
#     visited = [ [0]*len(maps[0]) for _ in range(len(maps)) ]
    
    # # 상 하 좌 우 (y, x)
    direction = [[-1, 0],[1, 0],[0, -1],[0, 1]]
    
    queue = deque()
    
    maps[0][0] = 2
    
    queue.append([0,0])

    while queue:
        # print(queue)
        # print(maps[0])
        # print(maps[1])
        # print(maps[2])
        # print(maps[3])
        # print(maps[4])
        
        cur_point = queue.popleft()
        
        my_point_i = cur_point[0]
        my_point_j = cur_point[1]
   
        # 상 하 좌 우
        for y, x in direction:
            # 범위를 벗어나지않고, 이동할 수 있으면(1) 이면 queue에 추가
            
            moved_point_i = my_point_i + y 
            moved_point_j = my_point_j + x
            
            if moved_point_i >= len(maps) or moved_point_i < 0:
                continue
            if moved_point_j  >= len(maps[0]) or moved_point_j < 0:
                continue
            if maps[moved_point_i][moved_point_j] != 1:
                continue
            # 최단거리 표시
            maps[moved_point_i][moved_point_j] = maps[my_point_i][my_point_j] + 1
            queue.append([moved_point_i,moved_point_j])
            
            # 최종 목적지에 도달하면 종료
            if [moved_point_i, moved_point_j] == [len(maps)-1, len(maps[0])-1]:
                return maps[-1][-1] - 1
    
    return -1
