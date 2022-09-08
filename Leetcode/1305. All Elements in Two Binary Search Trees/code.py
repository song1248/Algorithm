# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        answer = []
        
        def explore(node):

            tmp = []
                
            if not node:
                return []
            
            tmp.append(node.val)
            tmp.extend(explore(node.left))
            tmp.extend(explore(node.right))
        
            return tmp
        
        answer.extend(explore(root1))
        answer.extend(explore(root2))
        
        return sorted(answer)
