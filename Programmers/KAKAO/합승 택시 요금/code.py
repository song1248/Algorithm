# s에서 출발하여 A B를 모두 방문하는데 최소요금
# 모든 간선 정보가 주어진다
# (출발, 도착, 요금)
# 다익스트라로 해야될듯?
# 최단경로로만 이동해서 A, B둘다에 도달하면 종ㅀ

import copy
import heapq
def solution(n, s, a, b, fares):
    
    # 각 node에서 갈 수 있는 곳 & cost
    to_list = [[] for _ in range(n+1)]
    for n_1, n_2, cost in fares:
        to_list[n_1].append((n_2, cost))
        to_list[n_2].append((n_1, cost))
    
    # 각 node까지의 최단거리 구하기
    def dijkstra(start_node):
        distance = [ float('inf') for _ in range(n+1)]
        distance[start_node] = 0

        heap = []
        heapq.heappush(heap, start_node)

        while heap:

            cur_node = heapq.heappop(heap)
            cur_cost = distance[cur_node]

            for destination, cost in to_list[cur_node]:
                if cur_cost + cost >= distance[destination]:
                    continue
                distance[destination] = cur_cost + cost
                heapq.heappush(heap, destination)

        # A까지의 거리와 B까지의 거리를 return 
        return distance
    
    # A,B 까지의 거리
    answer = float('inf')
    distance = dijkstra(s)
#     print(distance)

    for i, d in enumerate(distance[1:]):
        i += 1
        distance_tmp = dijkstra(i)
#         print(distance_tmp)
        i_to_a = distance_tmp[a]
        i_to_b = distance_tmp[b]
        
        
        answer = min(answer, d+i_to_a+i_to_b )


    return answer
