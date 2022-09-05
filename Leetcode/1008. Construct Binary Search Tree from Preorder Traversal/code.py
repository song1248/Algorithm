# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder([i for i in preorder if i<root.val])
        root.right = self.bstFromPreorder([i for i in preorder if i>root.val])
        
        return root
