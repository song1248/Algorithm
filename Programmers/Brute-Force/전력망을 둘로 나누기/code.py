def solution(n, wires):
    
    # 간선 graph 생성
    graph = [[] for _ in range(n+1)]
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
    
    # print(graph)
    
    answer = float('inf')

    # start_node에서 갈 수 있는 각 간선으로 갈 수 있는 node 개수를 구한다.
    # = start node에서 각 간선방향 node에 대한 dfs 진행
    def explore(start_node):
        nonlocal n
        nonlocal graph

        tmp_answer = float('inf')
        
        for i in graph[start_node]:
            visited = [0 for _ in range(n+1)]
            visited[0] = 1      
            visited[start_node] = 1
            
            stack = []
            stack.append(i)
            
            size = 0
            
            while stack:
                
                node = stack.pop()
                
                visited[node] = 1
                
                for i in graph[node]:
                    # 방문하지 않았다면
                    if visited[i] == 0:
                        size += 1
                        stack.append(i)
            
            tmp_answer = min(tmp_answer,abs(n-size-size-2))
            # print(tmp_answer)
            
        return tmp_answer
         
    # start node를 바꿔가면서 탐색하여 가장 작은값을 찾는다.
    for start_node in range(1,n):
        # print("---------------------------------")
        answer = min(answer,explore(start_node))

    return answer
