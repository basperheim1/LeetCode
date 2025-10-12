class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n-1, -1, -1):
            if i == 0 and digits[i] == 9:
                digits[0] = 0
                return [1] + digits
            if digits[i] == 9:
                digits[i] = 0

            else:
                digits[i] += 1
                break

        return digits
        
