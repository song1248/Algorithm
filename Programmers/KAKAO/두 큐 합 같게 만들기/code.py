
from collections import deque

def solution(queue1, queue2):
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)  
    if sum1+sum2 % 2 == 1:
        return -1

    def counter(q1, q2, q_sum, half_sum = (sum1+sum2) //2):
        count = 0
        
        if not q1 or not q2:
            return float('inf')
        
        for i in range(3*len(q1)): 
            if q_sum > half_sum:
                poped = q1.popleft()
                q_sum -= poped
                q2.append(poped)
                
            elif q_sum < half_sum:
                poped = q2.popleft()
                q_sum += poped
                q1.append(poped)     
                
            else:
                return count
            
            count += 1     
                
        return float('inf')
                
    a = counter(deque(queue1), deque(queue2), sum1)    
    b = counter(deque(queue2), deque(queue1), sum2)
    
    answer = min(a,b)
    return -1 if answer == float('inf') else answer
