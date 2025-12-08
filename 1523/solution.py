class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0: 
            return (1 + high - low) // 2

        return ((high - low) // 2) + 1
