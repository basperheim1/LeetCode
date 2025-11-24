class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        total = 0
        result = []
        for num in nums: 
            total *= 2
            if num == 1: 
                total += 1

            if total % 5 == 0:
                result.append(True)
            else:
                result.append(False)

        return result 
