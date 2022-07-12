from collections import deque
def solution(s):
    answer = True
    
    queue = deque()
    
    for i in s:
        # print(i)
        if i == '(':
            queue.append(i)
        else:
            if not queue or queue.pop() != '(' :
                return False
        
    return False if queue else True
