class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen_nums = set()
        duplicates = []

        for num in nums: 
            if num in seen_nums: 
                duplicates.append(num)

            else:
                seen_nums.add(num)

        return duplicates 
