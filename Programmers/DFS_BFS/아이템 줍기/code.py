def solution(rectangle, characterX, characterY, itemX, itemY):
    
    # box_map 생성
    # map의 크기를  2배하여 탐색
    # (Nx,Ny), (Mx,M2) 의 box를 가질떄 2N-1 ~ 2M까지를 범위로 잡음 ★★★★
    # node와 간선관의 관계를 생각해야 한다
    
    map_size = 120
    box_map = [ [0 for _ in range(map_size)] for __ in range(map_size) ]
    for llx, lhy, rhx, rhy in rectangle:
        llx, lhy, rhx, rhy = 2*llx-1, 2*lhy-1, 2*rhx, 2*rhy
        for i in range(lhy, rhy):
            for j in range(llx, rhx):
                if box_map[i][j] == 1 or box_map[i][j] == -1:
                    box_map[i][j] = -1
                else:
                    box_map[i][j] = 1
        # 모퉁이 설정
        box_map[lhy][llx], box_map[lhy][rhx-1], box_map[rhy-1][llx], box_map[rhy-1][rhx-1]  = -1, -1, -1, -1
        
    # 최종위치 값 설정
    box_map[2*itemY-1][2*itemX-1] = float('inf')

    # 상하좌우 (그림의 y x 좌표에서)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    # 대각선
    directions2 = [(1,1),(1,-1),(-1,1),(-1,-1)]
    
    # 현재위치가 모서리인지 확인
    def is_edge(cur_y, cur_x):
        # 사각형 밖에있으면 모서리 아님
        if  box_map[cur_y][cur_x] == 0 :
            return False
        
        edge = False
        
        # 주변에 0이 있으면 모서리임(바깥쪽 모퉁이인지 확인)
        for dy, dx in directions:
            if box_map[cur_y+dy][cur_x+dx] == 0:
                return True
        
        # 안쪽 모퉁이인지 확인
        for dy, dx in directions2:
            if box_map[cur_y+dy][cur_x+dx] == 0:
                return True
      
        return False
    
    # 탐색
    def explore(cur_y, cur_x, move_count=3):

        # 모서리가 아니면 탐색하지 않음
        if is_edge(cur_y, cur_x) == False:
            return 0
        
        # 최종위치에 도달했는지 확인
        if [cur_y, cur_x] == [2*itemY-1, 2*itemX-1]:
            box_map[2*itemY-1][2*itemX-1] = min(box_map[2*itemY-1][2*itemX-1], move_count)
            return
        
        # 방문했던곳은 탐색하지 않음
        if box_map[cur_y][cur_x] > 1:
            return
        
        # 이동횟수 저장
        box_map[cur_y][cur_x] = move_count
            
        for dy, dx in directions:
            # 범위 밖으로는 이동하지 않음
            if cur_y+dy < 0 or cur_x+dx < 0 or cur_y+dy >= map_size or cur_x+dx >= map_size:
                continue
            # 이동 횟수는 현재 이동횟수 + 1    
            move_count = box_map[cur_y][cur_x] + 1
            explore(cur_y+dy, cur_x+dx, move_count)     
        return
    
    # 탐색
    explore(2*characterY-1, 2*characterX-1)
    
    # map을 2배하여 계산하였음으로 2로 나누어주어 값을 구함
    return int((box_map[2*itemY-1][2*itemX-1])/2-1)
