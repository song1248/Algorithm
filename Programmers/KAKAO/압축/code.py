from collections import defaultdict

def solution(msg):
    
    answer = []
    
    alpha_dict = defaultdict()
    
    for i in range(ord('A'), ord('Z')+1):
        alpha_dict[chr(i)] =  i - ord('A') + 1
    
    idx = 27
    
    i = 0
    while i < len(msg):
        chr_num = 1
        while msg[i:i+chr_num] in alpha_dict and i+chr_num <= len(msg): 
            chr_num += 1
        answer.append(alpha_dict[msg[i:i+chr_num-1]])
        alpha_dict[msg[i:i+chr_num]] = idx
        idx += 1
        
        i = i + chr_num -1

    return answer
