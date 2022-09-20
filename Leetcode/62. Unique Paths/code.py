from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        r_map = [[ 0 for _ in range(n) ]for  _ in range(m)]

        
        Q = deque([[0,0]])
        
        while Q:
            
            cur_i, cur_j = Q.popleft()
            
            if cur_i < 0 or cur_j < 0 or cur_i >= m or cur_j >= n:
                continue
            
            if r_map[cur_i][cur_j]:
                continue
            
            if  cur_i > 0 and cur_j >0:
                r_map[cur_i][cur_j] = r_map[cur_i-1][cur_j] + r_map[cur_i][cur_j-1]
            elif cur_i > 0:
                r_map[cur_i][cur_j] = r_map[cur_i-1][cur_j]
            elif cur_j > 0:
                r_map[cur_i][cur_j] = r_map[cur_i][cur_j-1]
            else:
                r_map[cur_i][cur_j] = 1

                            
            for dy, dx in [[1,0],[0,1]]:
                Q.append([cur_i+dy, cur_j+dx])

        
        return r_map[-1][-1]
