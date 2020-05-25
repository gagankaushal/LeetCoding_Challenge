# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def helper(lower = float('-inf'), higher = float('inf')):
            nonlocal idx
            
            # 1. if the current node is the last one
            if idx == n:
                return None
            
            
            val = preorder[idx]
            
            # 2. if the node's value doesn't satisfy the conditions of BST
            if val < lower or val > higher:
                return None
            
            # Actual implementation of the ques
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower,val)
            root.right = helper(val,higher)
            
            
            return root
            
        
        idx = 0
        
        n = len(preorder)
        
        return helper()
        
