from collections import defaultdict
import heapq
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        tree_dict = defaultdict(list)
        sum_dict = defaultdict(list) # [idx, count]
        heap_dict = defaultdict(list) # 다른 value를 가진 것들의 최장길이를 저장
        
        for node_idx, p in enumerate(parent):
            tree_dict[p].append(node_idx)
  
        # -1 값이 들어갈때 예외처리를 위함
        s += '#'
        
        def explore(node_idx = 0, count = 0):
            # print(node_idx)
            
            parent_node = parent[node_idx]
            cur_val = s[node_idx]
            parent_val = s[parent_node]
            
            # 현재 노드의 자식노드로 이동
            for c_node_idx in tree_dict[node_idx]:
                # key : 부모노드
                # value :  [자식노드idx, max_sum]
                sum_dict[node_idx].append([c_node_idx, explore(c_node_idx, count)])
             
            max_sum = 1
            for c_node_idx, sum_num in sum_dict[node_idx]:
                # 현재 노드와 자식 노드가 다르면
                if s[node_idx] != s[c_node_idx]:
                    heapq.heappush(heap_dict[node_idx] ,-sum_num)
                    max_sum = max(sum_num+1, max_sum)
                     
            return max_sum
        
        explore()
        
        # heap에서 최대값 두개 더한것 + 1
        answer = -1
        for value in heap_dict.values():
            count = 0
            max_sum = -1
            while value and count < 2:
                max_sum += heapq.heappop(value)
                count += 1
            
            answer = min(max_sum, answer)
        
        return -answer
