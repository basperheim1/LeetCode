class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_seen = 0
        for num in nums: 
            if num == val: 
                val_seen += 1
        
        for i in range(val_seen):
            nums.remove(val)
