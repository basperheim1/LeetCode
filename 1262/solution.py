class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        max_sum = sum(nums)
        if max_sum % 3 == 0: 
            return max_sum 

        if max_sum % 3 == 1: 

            min_one = None
            min_two = []
            for num in nums: 
                if num % 3 == 1: 
                    if min_one is None: 
                        min_one = num 

                    else:
                        if num < min_one: 
                            min_one = num 

                if num % 3 == 2: 
                    if len(min_two) != 2: 
                        min_two.append(num)

                    else:
                        if min_two[1] > num: 
                            min_two[1] = num

                    min_two.sort()

            if min_one is None: 
                if len(min_two) != 2: 
                    return 0

                return max_sum - sum(min_two)

            if len(min_two) != 2: 
                return max_sum - min_one

            if sum(min_two) < min_one: 
                return max_sum - sum(min_two)

            return max_sum - min_one

        if max_sum % 3 == 2: 

            min_one = None
            min_two = []
            for num in nums: 
                if num % 3 == 2: 
                    if min_one is None: 
                        min_one = num 

                    else:
                        if num < min_one: 
                            min_one = num 

                if num % 3 == 1: 
                    if len(min_two) != 2: 
                        min_two.append(num)

                    else:
                        if min_two[1] > num: 
                            min_two[1] = num

                    min_two.sort()

            if min_one is None: 
                if len(min_two) != 2: 
                    return 0

                return max_sum - sum(min_two)

            if len(min_two) != 2: 
                return max_sum - min_one

            if sum(min_two) < min_one: 
                return max_sum - sum(min_two)

            return max_sum - min_one
