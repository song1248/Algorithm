def solution(a):
    
    min_set = set()
    
    min_num = float('inf')
    for i, num in enumerate(a):
        idx = i    
        if min_num > num:
            min_num =  num
            min_set.add(idx)
      
    min_num = float('inf')
    for i, num in enumerate(a[::-1]):
        idx = len(a) - 1 - i
        if min_num > num:
            min_num =  num
            min_set.add(idx)
        
    return len(min_set)
