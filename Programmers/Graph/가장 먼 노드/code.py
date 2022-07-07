import heapq

def solution(n, edge):

    distance = [float('inf')] * (n+1)
    
    # O(n)의 시간복잡도로 graph 만들기
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    
#     # O(n^2)의 시간복잡도로 graph 만들기
#     graph = [ []  for _ in range(n)]
#     for i in range(n):
#         for j, e in enumerate(edge):
#             if i == e[0]-1:
#                 graph[i].append(e[1])       
#             if i == e[1]-1:
#                 graph[i].append(e[0])
#     a = [[]] 
#     a.extend(graph)
    
    
#     print(graph)
#     print(distance)
    
    
    heap = []
    distance[1] = 0
    heapq.heappush(heap,[0,1])

    while heap:
        # print(q)
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for n in graph[now]:
            cost = 1 + dist
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(heap,[cost,n])
                
                
    
    return distance.count(max(distance[1:]))
