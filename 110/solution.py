# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        

    def _isBalanced(self, currentNode, balanced) -> bool:
        if not currentNode: 
            return 0
        left_height = self._isBalanced(currentNode.left, balanced)
        right_height = self._isBalanced(currentNode.right, balanced)

        if abs(left_height - right_height) > 1: 
            balanced[0] = False 

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        self._isBalanced(root, balanced)
        return balanced[0]
