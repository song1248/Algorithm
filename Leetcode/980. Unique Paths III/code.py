import copy

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:    
        
        len_row = len(grid)
        len_col = len(grid[0])
        
        # copy의 시간복잡도를 줄이기위해 1차원 배열이용
        one_dim_grid = [ True for _ in range(len_row*len_col)]
        
        # start_point, start_point, path_count(장애물 수)구하기
        start_point = [] 
        end_point = []
        path_count = 1
        for row in range(len_row):
            for col in range(len_col):
                if grid[row][col] == 1:
                    start_point = [row,col] 
                if grid[row][col] == 2:
                    end_point = [row,col]
                if grid[row][col] == -1:
                    one_dim_grid[row * len_col + col] = False
                    path_count += 1
        
        # DFS
        stack = [[start_point[0], start_point[1], path_count, one_dim_grid]]
        answer = 0
        
        while stack:
            
            cur_i, cur_j, path_count, grid = stack.pop()
            
            # 예외처리
            if cur_i >= len_row or cur_j >= len_col or cur_i < 0 or cur_j < 0:
                continue
            
            # 방문 & 벽 처리
            if not grid[cur_i * len_col + cur_j]:
                continue
            tmp_grid = grid.copy()
            tmp_grid[cur_i * len_col + cur_j] = False
            
            # answer 조건
            if path_count == len_row * len_col and [cur_i, cur_j] == end_point:
                answer += 1    
    
            for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                stack.append([cur_i+dy, cur_j+dx, path_count+1, tmp_grid])
                
        return answer
