class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)

        indexes = dict()
        nums.sort()
        for index in range(n): 
            num = nums[index]
            if num not in indexes: 
                indexes[num] = [index, index]

            else:
                indexes[num][1] = index

        if len(nums) == 1: 
            return 1

        elif len(nums) == 2:
            if nums[1] - nums[0] <= k and numOperations != 0: 
                return 2

            if nums[1] - nums[0] <= 2*k and numOperations > 1: 
                return 2

            else:
                return 1 

        new_nums = [[num, True] for num in nums] 

        for i in range(n):
            current_num = nums[i]
            new_nums.append([current_num - k, False])
            new_nums.append([current_num + k, False])

        new_nums.sort(key = lambda x: x[0])

        nums = [num[0] for num in new_nums]
        valid = [num[1] for num in new_nums]

        n = len(nums)

        max_frequency = 1
        left_pointer = 0
        right_pointer = 2

        fake_vals = 0
        if not valid[0]:
            fake_vals += 1
        if not valid[1]:
            fake_vals += 1
            
        for i in range(1, n):
            middle_pointer = i

            current_val = nums[middle_pointer]
            while current_val - nums[left_pointer] > k:
                if not valid[left_pointer]:
                    fake_vals -= 1
                left_pointer += 1

            while right_pointer != n and nums[right_pointer] - current_val <= k:
                if not valid[right_pointer]:
                    fake_vals += 1
                right_pointer += 1

            if current_val in indexes: 
                for_sure_vals = indexes[current_val][1] - indexes[current_val][0] + 1

            else:
                for_sure_vals = 0

            possible_vals = right_pointer - left_pointer - for_sure_vals - fake_vals
            max_frequency = max(max_frequency, for_sure_vals + min(possible_vals, numOperations))


        return max_frequency


        

