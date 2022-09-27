def solution(n, arr1, arr2):
    
    j_map = [ [' ' for _ in range(n)]for _ in range(n)]
    
    for i, num in enumerate(arr1):
        for j, s in enumerate(str(bin(num)[2:].zfill(n))):
            
            if s == '1':
                j_map[i][j] = '#'

    for i, num in enumerate(arr2):
        for j, s in enumerate(str(bin(num)[2:].zfill(n))):
            if s == '1':
                j_map[i][j] = '#'
        
    

    return [ ''.join(i) for i in j_map ]
