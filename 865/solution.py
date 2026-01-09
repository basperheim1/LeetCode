# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def treeSize(self, node, node_height, height, smallest_root, min_height) -> bool: 
        if node is None: 
            return False 

        # print(node_height)
        # print(node.val)
        # print()

        if node_height == height: 
            if min_height is None: 
                smallest_root[0] = node
                min_height = height
            return True

        left_contains = self.treeSize(node.left, node_height + 1, height, smallest_root, min_height)
        right_contains = self.treeSize(node.right, node_height + 1, height, smallest_root, min_height)


        contains = left_contains or right_contains
        both = left_contains and right_contains

        if both: 
            if min_height is None: 
                min_height = height
                smallest_root[0] = node

            else:
                if height < min_height:
                    min_height = height
                    smallest_root[0] = node

        return contains


        

    def determineHeight(self, node, node_height) -> int: 
        if node is None: 
            return node_height

        return max(self.determineHeight(node.left, node_height + 1), self.determineHeight(node.right, node_height + 1))

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        height = self.determineHeight(root, -1)
        # print(height)
        # print()
        smallest_root = [None]
        self.treeSize(root, 0, height, smallest_root, None)
        return smallest_root[0]


