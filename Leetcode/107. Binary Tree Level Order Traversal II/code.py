
from collections import defaultdict

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer_dict = defaultdict(list)
        max_layer = 0
        answer = []
        
        def move(node = root, layer = 1):
            nonlocal max_layer
            nonlocal answer
            
            max_layer = max(layer, max_layer)
            
            if node.val is not None:
                answer_dict[layer].append(node.val)
                
            if node.left:
                move(node.left, layer + 1)
            if node.right:
                move(node.right, layer + 1)
        
        if root:
            move()
        else:
            return []
        
        for i in range(max_layer,0,-1):
            answer.append(answer_dict[i])
            
        return answer
