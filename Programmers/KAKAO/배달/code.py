# N개의 마을에서 K시간 이하로 배달

import heapq
from collections import defaultdict

def solution(N, road, K):
    answer = 0
    
    # 출발지 : [시간, 도착지]
    road_dict = defaultdict(list)
    for s, d, t in road:
        road_dict[s].append([t, d])
        road_dict[d].append([t, s])
    
    heap = [[0,1]]
    visited = [float('inf') for i in range(N)]
    
    while heap:
        
        cur_t, cur_node = heapq.heappop(heap)
        
        if visited[cur_node-1] <= cur_t:
            continue
            
        visited[cur_node-1] = cur_t

        for t, d in road_dict[cur_node]:
            heapq.heappush(heap, [cur_t+t, d])
        
    return len(list(filter(lambda x : K >= x , visited )))
