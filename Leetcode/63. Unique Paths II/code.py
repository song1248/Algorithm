from collections import deque
# import deque

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        answer = 0
        # robo_map = [[ 0 for _ in obstacleGrid[0] ] for _ in obstacleGrid]
        
        Q = deque()
        
        Q.append([0, 0])
        
        while Q:

            cur_i, cur_j = Q.popleft()
            
            # 방문처리
            try:
                if obstacleGrid[cur_i][cur_j] < 0 or obstacleGrid[cur_i][cur_j] == 1:
                    continue
            except:
                continue
            
                
            try:
                up = 0 if obstacleGrid[cur_i-1][cur_j] == 1 else obstacleGrid[cur_i-1][cur_j]
            except:
                up = 0
            try:
                left = 0 if obstacleGrid[cur_i][cur_j-1] == 1 else obstacleGrid[cur_i][cur_j-1]
            except:
                left = 0
                
            obstacleGrid[cur_i][cur_j] = up + left + (-1 if [cur_i, cur_j] == [0,0] else 0)
            
            # 탐색
            for dy, dx in [[1,0],[0,1]]:
                Q.append([cur_i + dy, cur_j + dx])
                    
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] < 0:
            answer = -obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
        else:
            answer = 0
            
        return answer
