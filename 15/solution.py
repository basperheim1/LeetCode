from typing import Dict, List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        totals_needed: Dict[int, List[int]] = dict()
        n = len(nums)

        if nums == [0]*n:
            return [[0, 0, 0]]

        triplets = set()
        for i in range(n): 
            current_num = nums[i]*-1
            
            if current_num in totals_needed:
                totals_needed[current_num].append(i)
                
            else:
                totals_needed[current_num] = [i]
            
        for i in range(n):
            for j in range(i+1, n):
                
                total = nums[i] + nums[j]
                if (nums[i], nums[j], -1*total) in totals_needed:
                    continue

                if total in totals_needed:
                    for index in totals_needed[total]:
                        if index != i and index != j: 
                            triplet = [nums[i], nums[j], nums[index]]
                            triplet.sort()
                            triplets.add(tuple(triplet))
                            break
                            
        return [list(triplet) for triplet in triplets] 