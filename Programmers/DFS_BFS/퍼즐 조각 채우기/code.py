import copy
from functools import lru_cache
def solution(game_board, table):
    
    # 90도 회전 함수
    def rotate_90(m):
        ret = list(zip(*m[::-1]))
        return ret    

    direction = [(1,0),(0,-1),(-1,0),(0,1)]
    
    # 가능한 shape list 모두 찾기
    def make_shape_list(basic_map, find_point=0):
        
        # shape 하나 찾기
        def find_shape(i,j, point = 0):
            nonlocal max_x
            nonlocal max_y
            nonlocal min_x
            nonlocal min_y
            nonlocal block_list

            # 방문했거나, block이 없는 장소이면 탈출
            if basic_map[i][j] == point:
                return

            basic_map[i][j] = point

            # 상하좌우로 이동
            for dy, dx in direction:
                if i+dy >= len(table) or j+dx >= len(table[0]) or i+dy < 0 or j+dx < 0:
                    continue
                find_shape(i+dy, j+dx, point)

            max_y = max(max_y, i)
            max_x = max(max_x, j)
            min_y = min(min_y, i)
            min_x = min(min_x, j)
            block_list.append((i,j))
            return 
        
        # 돌아가면서 가능한 전체 shape 찾기
        shape_list = []
        for i in range(len(basic_map)):
            for j in range(len(basic_map)):
                max_x = 0
                max_y = 0
                min_x = 100
                min_y = 100
                block_list = []
                find_shape(i, j, find_point)
                # 배경은 0
                blcok_background = [[0 for __ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
                if block_list:
                    # 속은 1
                    for py, px in block_list:
                        blcok_background[py-min_y][px-min_x] = 1
                    # 4방향 회전 
                    tmp = []
                    for _ in range(4):
                        tmp.append(blcok_background)
                        blcok_background = rotate_90(blcok_background)

                    shape_list.append(tmp)
                    
        return shape_list
    
    '''
    puzzle 조각 찾기
    '''
   
    table_shape_list = make_shape_list(table, find_point=0)
    game_board_shape_list = make_shape_list(game_board, find_point=1) 

 
		# 같은 조각이 있는지 완전탐색
    answer_list = []
    m = 0
    while m < len(table_shape_list):
        m_deleted = False
        n = 0
        while m < len(table_shape_list) and n < len(game_board_shape_list):
            n_deleted = False
            for i in range(4):
                # 일치하는것이 있는지확인
                # 일치하는게 있었다면 제거

                if table_shape_list[m][i] in game_board_shape_list[n]:

                    answer_list.append(table_shape_list[m][0])
                    table_shape_list.pop(m)
                    game_board_shape_list.pop(n)
                    m_deleted = True
                    n_deleted = True
                    break
    
            if n_deleted:
                continue
            n += 1
        if m_deleted:
            continue
        m += 1
    
    answer = 0
    for a in answer_list:
        for b in a:
            answer += b.count(1)
                    
    return answer
