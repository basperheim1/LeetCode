class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left_pointer = 0
        right_pointer = n - 1

        max_area = 0
 
        while left_pointer != right_pointer: 
            possible_area = (right_pointer - left_pointer)*min(height[left_pointer], height[right_pointer])

            max_area = max(max_area, possible_area)

            if height[left_pointer] > height[right_pointer]:
                right_pointer -= 1

            else:
                left_pointer += 1

        return max_area
