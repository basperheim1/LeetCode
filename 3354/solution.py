class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums) 

        current_total = 0
        possible_solutions = 0
        for i in range(len(nums)):
            current_num = nums[i]

            if current_num == 0: 
                if total % 2 == 0 and current_total == total / 2:
                    possible_solutions += 2

                elif total % 2 == 1 and (current_total == total // 2 or current_total == (total // 2) + 1):
                    possible_solutions += 1

            else:
                current_total += current_num 

        return possible_solutions 
