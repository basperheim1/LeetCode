# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_s = set(nums)

        prev_node = None 
        current_node = head
        head_node = None 

        while current_node is not None: 
            if current_node.val in nums_s: 
                current_node = current_node.next 
                continue

            if head_node is None: 
                head_node = current_node

            else:
                prev_node.next = current_node 


            prev_node = current_node 
            current_node = current_node.next 
            prev_node.next = None 

        return head_node 

            
