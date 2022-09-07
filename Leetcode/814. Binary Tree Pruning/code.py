# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def explore(node = root):
            
            # node가 없으면
            if not node:
                return
            
            # 좌, 우 자식 node 탐색
            node.left, node.right = explore(node.left), explore(node.right)
            
            
            if any([node.val, node.left, node.right]):
                return node
            else: # 0혹은 none 뿐이면 None을 반환
                return None
            
        return explore()
            
# class Solution:
#     def pruneTree(self, n):
#         if n:
#             n.left, n.right = self.pruneTree(n.left), self.pruneTree(n.right)
#             return n if any([n.val, n.left, n.right]) else None
   
