from collections import defaultdict
import math

def solution(fees, records):
    
    
    
    c_dict = defaultdict(list)
    b_dict = defaultdict(int)
    sum_dict = defaultdict(int)
    
    for i, record in enumerate(records):
        tmp = record.split(' ')
        tmp[0] = tmp[0].split(':')
        tmp[0] = int(tmp[0][0])*60 + int(tmp[0][1])
        records[i] = tmp
        
        t, n, io = tmp
        
        c_dict[n].append([t,io])
    
    for key in c_dict.keys():
        idx = 0
        while idx == len(c_dict[key]):
            if idx % 2 == 0 and c_dict[key][idx][1] == 'IN':
                c_dict[key].insert(idx, [23*60+59, 'OUT'])
                continue
            idx += 1
            
        if c_dict[key][-1][1] == 'IN':
            c_dict[key].append([23*60+59, 'OUT'])
     
    answer = []
    for key in sorted(c_dict.keys()):
        # 누적 시간 계산
        for i in range(len(c_dict[key])//2):
            i = i*2
            sum_dict[key] += c_dict[key][i+1][0] - c_dict[key][i][0]
        
        # 누적 요금 계산
        if sum_dict[key] <= fees[0]:
            b_dict[key] = fees[1]
        elif sum_dict[key] > fees[0]:
            b_dict[key] = fees[1] + math.ceil((sum_dict[key] - fees[0]) / fees[2])*fees[3]
        
        answer.append(b_dict[key])


    return answer
