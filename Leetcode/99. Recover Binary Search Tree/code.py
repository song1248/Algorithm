# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,arr):  # return sorted array of nodes
        if not root:
            return 
        self.inorder(root.left,arr)
        arr.append(root)
        self.inorder(root.right,arr)
        return arr

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res = self.inorder(root,[])
        n = len(res)

        a = res[0]      # default 1st wrong value from start
        for i in range(1,n):
            if res[i].val < res[i-1].val:
                a = res[i-1]
                break

        b = res[-1]   #default 1st wrong value from end
        for i in range(n-2,-1,-1):
            if res[i].val > res[i+1].val:
                b = res[i+1]
                break
        a.val,b.val = b.val,a.val       # swap
