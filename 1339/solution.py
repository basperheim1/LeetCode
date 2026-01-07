# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def totalSum(self, node) -> int: 
        if node is None: 
            return 0

        left_sum = self.totalSum(node.left)
        right_sum = self.totalSum(node.right)

        return left_sum + right_sum + node.val

    def maxSum(self, node, total_sum, max_prod_list) -> int: 
        if node is None: 
            return 0

        left_sum = self.maxSum(node.left, total_sum, max_prod_list)
        right_sum = self.maxSum(node.right, total_sum, max_prod_list)

        current_sum = node.val + left_sum + right_sum
        other_sum = total_sum - current_sum 

        max_prod = max_prod_list[0]

        if current_sum * other_sum > max_prod: 
            max_prod_list[0] = current_sum * other_sum

        return current_sum
            

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = self.totalSum(root)
        max_prod_list = [0]
        self.maxSum(root, total_sum, max_prod_list)

        return max_prod_list[0] % (10**9 + 7)
