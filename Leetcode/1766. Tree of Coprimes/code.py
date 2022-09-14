from collections import defaultdict
import copy
from collections import deque

# 최대공약수가 1 인 가장 가까운 노드 찾기
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        
        # 정답리스트
        answer = [-1]*len(nums)
        answer[0] = -1
        
        # tree 만들기
        node_dict = defaultdict(set)
        
        # O(n)
        for s_node, e_node in edges:
            node_dict[s_node].add(e_node)
            node_dict[e_node].add(s_node)
        
        # O(2n)
        def make_tree(node = 0):
            for i in node_dict[node]:
                node_dict[i].discard(node)
            for i in node_dict[node]:
                make_tree(i)     
        make_tree()       
          
        # gcd 리스트
        gcdset = [set() for i in range(51)]
        for i in range(1,51):
            for j in range(1,51):
                if math.gcd(i,j) == 1:
                    gcdset[i].add(j)
                    gcdset[j].add(i)
        
        # print(gcdset)
             
        def explore(node = 0, node_list = deque()):
            nonlocal answer
            
            cur_num = nums[node]
            
            # 현재 노드의 약수가 num_dict의 key 에 있는지 확인
            
            
            # 조상 탐색
            for prv_node in node_list:
                
                # 최대공약수가 1 인지 확인 -> 1이면
                prv_num = nums[prv_node]
                if prv_num in gcdset[cur_num]:
                    answer[node] = prv_node
                    break

            
            # 조상복사
            node_list = node_list.copy()
            node_list.appendleft(node)
            
            
            for next_node in node_dict[node]:
                explore(next_node, node_list)
    
        explore()
        
        return answer
            
