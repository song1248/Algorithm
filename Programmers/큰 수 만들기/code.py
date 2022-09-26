from collections import deque

def solution(number, k):
    
    Q = deque()
       
    for n in number:
        if k == 0:
            Q.append(n)
            continue
        if not Q:
            Q.append(n)
            continue 
        while Q and  k > 0 and int(n) > int(Q[-1]):
            Q.pop()
            k -= 1
            
        Q.append(n)
    
    while k >0:
        Q.pop()
        k -= 1
            
    return ''.join(Q)
