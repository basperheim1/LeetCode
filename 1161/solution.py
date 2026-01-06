# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = 1
        max_value = root.val 
        current_value = 0
        current_level = 1

        q = deque()

        q.append((root, 1)) 

        while len(q) >= 0: 

            if len(q) == 0: 
                if current_value > max_value: 
                    return current_level 

                return max_level
            
            current_node, level = q.popleft()

            if level > current_level:
                current_level = level 
                if current_value > max_value:
                    max_level = level - 1
                    max_value = current_value 
                current_value = 0
                

            current_value += current_node.val 

            if current_node.left: 
                q.append((current_node.left, level + 1))

            if current_node.right: 
                q.append((current_node.right, level + 1))

        return max_level 
