"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        layer_list = [False for _ in range(100)]
        
        Q = deque()
        Q.append([root, 0])
        
        while Q:
            poped_node, layer = Q.popleft()
            
            if not poped_node:
                continue

            if Q and Q[0][1] == layer:
                poped_node.next = Q[0][0]
            else:
                poped_node.next = None
            
            Q.append([poped_node.left, layer+1])
            Q.append([poped_node.right, layer+1])
        
        return root
