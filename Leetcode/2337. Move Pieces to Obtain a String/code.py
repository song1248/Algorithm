class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # start를 target의 형태로만들기
        # L은 왼쪽의 '_'으로만 이동가능
        # R은 오른쪽의 '_'으로만 이동가능
     
        if ''.join(start.split('_')) != ''.join(target.split('_')):
            return False
            
        s_L_list = deque()
        s_R_list = deque()
        for i, LR in enumerate(start):
            if LR == 'L':
                s_L_list.append(i)
            if LR == 'R':
                s_R_list.append(i)   
                
        t_L_list = deque()
        t_R_list = deque()
        for i, LR in enumerate(target):
            if LR == 'L':
                t_L_list.append(i)
            if LR == 'R':
                t_R_list.append(i)
                

        while True:
            
            if not s_L_list and not t_L_list and not s_R_list and not t_R_list:
                break
            
            s_L = 0
            t_L = 0
            s_R = 0
            t_R = 0
            
            if s_L_list and t_L_list:
                s_L = s_L_list.popleft()
                t_L = t_L_list.popleft()
            
            if s_R_list and t_R_list:
                s_R = s_R_list.popleft()
                t_R = t_R_list.popleft()
            
            if s_L < t_L:
                return False
            if s_R > t_R:
                return False     
            
        return True
