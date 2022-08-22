
from collections import deque
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # 이전 가능한 네모들의 모든합을 dp에 저장
        
        answer = 0
        
        def bfs(start_i, start_j):
            nonlocal answer
            
            visited = [[False for _ in matrix[0]] for _ in matrix]
            dp = [[0 for _ in matrix[0]] for _ in matrix]

            Q = deque()

            # i, j, sum
            Q.append([start_i,start_j])

            while Q:

                cur_i, cur_j = Q.popleft()
                    
                # 범위 밖
                if cur_i >= len(matrix) or cur_j >= len(matrix[0]):
                    continue
                
                # 방문처리
                if visited[cur_i][cur_j]:
                    continue
                visited[cur_i][cur_j] = True
                
                # 합 구하기
                left = 0 if cur_i - 1 < 0 else dp[cur_i - 1][cur_j]
                up = 0 if cur_j - 1 < 0 else dp[cur_i][cur_j - 1]
                left_up = 0 if cur_i - 1 < 0 or cur_j - 1 < 0 else dp[cur_i-1][cur_j-1]          
                dp[cur_i][cur_j] = matrix[cur_i][cur_j] + left + up - left_up

                if dp[cur_i][cur_j] == target:
                    answer += 1
                
                for dy, dx in [[1,0],[0,1]]:
                    Q.append([cur_i+dy, cur_j+dx])
                    
           
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                bfs(i, j)
        
        return answer
